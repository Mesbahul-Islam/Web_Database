from __future__ import annotations

import importlib
from datetime import date, datetime
from uuid import uuid4

import pytest
from sqlalchemy import func, inspect

from app.models.user import User, RoleEnum
from app.security.utils import get_password_hash
from app.security.token import create_access_token


def _serialize_value(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return value


def _get_model_for_route(route):
    module = importlib.import_module(route.endpoint.__module__)
    return getattr(module, "Model", None)


def _routes_by_module(app):
    buckets = {}
    for route in app.router.routes:
        methods = getattr(route, "methods", set())
        if not methods:
            continue
        buckets.setdefault(route.endpoint.__module__, []).append(route)
    return buckets


def _get_primary_key_column(model):
    pk_cols = list(inspect(model).primary_key)
    if len(pk_cols) != 1:
        return None
    return pk_cols[0]


def _next_pk_value(db_session, model, pk_col):
    try:
        py_type = pk_col.type.python_type
    except Exception:
        return None

    if py_type is int:
        max_val = db_session.query(func.max(pk_col)).scalar()
        return int(max_val or 0) + 1
    if py_type is str:
        return f"test_{uuid4().hex[:12]}"
    return None


def _row_to_payload(row, model):
    payload = {}
    for col in model.__table__.columns:
        payload[col.name] = _serialize_value(getattr(row, col.name))
    return payload


def _apply_unique_overrides(payload, model):
    for col in model.__table__.columns:
        if not col.unique or col.name not in payload:
            continue
        value = payload[col.name]
        if isinstance(value, str):
            payload[col.name] = f"{value}-test"
        elif isinstance(value, int):
            payload[col.name] = value + 1


def _find_route(routes, method: str, requires_param: bool):
    for route in routes:
        methods = getattr(route, "methods", set())
        if method not in methods:
            continue
        if ("{" in route.path) != requires_param:
            continue
        return route
    return None


def _replace_path_param(route_path: str, route, value: str):
    path = route_path
    for param in route.dependant.path_params:
        path = path.replace(f"{{{param.name}}}", value)
    return path


def _pick_update_field(model, pk_name: str):
    for col in model.__table__.columns:
        if col.name == pk_name:
            continue
        try:
            py_type = col.type.python_type
        except Exception:
            continue
        if py_type in {str, int}:
            return col
    return None


def test_post_put_delete_endpoints(client, db_session):
    username = f"crud-test-{uuid4().hex[:12]}"
    user = User(
        username=username,
        password=get_password_hash("crud-test-password"),
        role_name=RoleEnum.USER,
    )
    db_session.add(user)
    db_session.commit()
    token = create_access_token(data={"sub": username})
    headers = {"Authorization": f"Bearer {token}"}

    for module_name, routes in _routes_by_module(client.app).items():
        if module_name.endswith(".auth"):
            continue
        post_route = _find_route(routes, "POST", requires_param=False)
        if post_route is None:
            continue

        put_route = _find_route(routes, "PUT", requires_param=True)
        delete_route = _find_route(routes, "DELETE", requires_param=True)
        assert put_route is not None, f"Missing PUT route for module {module_name}"
        assert delete_route is not None, f"Missing DELETE route for module {module_name}"

        model = _get_model_for_route(post_route)
        if model is None:
            continue

        pk_col = _get_primary_key_column(model)
        if pk_col is None:
            pytest.skip(f"Composite or missing PK for {model}")

        seed_row = db_session.query(model).first()
        if seed_row is None:
            pytest.skip(f"No seed data for {model}")

        payload = _row_to_payload(seed_row, model)
        new_pk = _next_pk_value(db_session, model, pk_col)
        if new_pk is None:
            pytest.skip(f"Unsupported PK type for {model}")
        payload[pk_col.name] = new_pk
        _apply_unique_overrides(payload, model)

        response = client.post(post_route.path, json=payload, headers=headers)
        assert response.status_code in {200, 201}, f"POST {post_route.path} failed: {response.status_code}"

        update_col = _pick_update_field(model, pk_col.name)
        if update_col is not None:
            update_payload = payload.copy()
            if isinstance(update_payload[update_col.name], str):
                update_payload[update_col.name] = f"{update_payload[update_col.name]}-updated"
            elif isinstance(update_payload[update_col.name], int):
                update_payload[update_col.name] = update_payload[update_col.name] + 1

            put_path = _replace_path_param(put_route.path, put_route, str(new_pk))
            response = client.put(put_path, json=update_payload, headers=headers)
            assert response.status_code == 200, f"PUT {put_path} failed: {response.status_code}"

        delete_path = _replace_path_param(delete_route.path, delete_route, str(new_pk))
        response = client.delete(delete_path, headers=headers)
        assert response.status_code in {200, 204}, f"DELETE {delete_path} failed: {response.status_code}"

    db_session.delete(user)
    db_session.commit()
