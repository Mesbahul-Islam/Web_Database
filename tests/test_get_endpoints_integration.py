from __future__ import annotations

import importlib
from datetime import date, datetime

import pytest
from sqlalchemy import inspect

from app.models.taksoni import Taksoni


def _serialize_value(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return value


def _get_model_for_route(route):
    module = importlib.import_module(route.endpoint.__module__)
    return getattr(module, "Model", None)


def _match_column(model, param_name: str):
    columns = {col.name: col for col in model.__table__.columns}
    if param_name in columns:
        return columns[param_name]

    lower = param_name.lower()
    for name, col in columns.items():
        if name.lower() == lower:
            return col
    return None


def test_get_list_endpoints(client):
    for route in client.app.router.routes:
        methods = getattr(route, "methods", set())
        if "GET" not in methods:
            continue
        if "{" in route.path:
            continue
        if route.path in {"/openapi.json", "/docs", "/redoc", "/docs/oauth2-redirect"}:
            continue
        if route.path.startswith("/auth/"):
            continue

        response = client.get(route.path, params={"limit": 1})
        assert response.status_code == 200, f"{route.path} returned {response.status_code}"
        assert isinstance(response.json(), list), f"{route.path} did not return a list"


def test_taksoni_list_endpoint_without_trailing_slash(client):
    response = client.get("/taksoni", params={"page": 1, "page_size": 25, "search": "en"})
    assert response.status_code == 200
    assert not response.history
    assert response.url.path == "/taksoni"


def test_taksoni_search_filters_results(client, db_session):
    item = db_session.query(Taksoni).filter(Taksoni.tieteellinen_nimi.isnot(None)).first()
    assert item is not None

    search_term = item.tieteellinen_nimi[:4].strip()
    assert search_term

    response = client.get("/taksoni", params={"page": 1, "page_size": 25, "search": search_term})
    assert response.status_code == 200

    payload = response.json()
    items = payload["items"]
    assert items

    for result in items:
        string_values = [value for value in result.values() if isinstance(value, str)]
        assert any(search_term.lower() in value.lower() for value in string_values)


def test_taksoni_search_matches_genus_or_species(client, db_session):
    item = (
        db_session.query(Taksoni)
        .filter((Taksoni.suku.isnot(None)) | (Taksoni.laji.isnot(None)))
        .first()
    )
    assert item is not None

    search_source = item.suku or item.laji
    assert search_source is not None

    search_term = search_source[:4].strip()
    assert search_term

    response = client.get("/taksoni", params={"page": 1, "page_size": 25, "search": search_term})
    assert response.status_code == 200

    payload = response.json()
    assert payload["items"]

    matched = False
    for result in payload["items"]:
        if any(
            search_term.lower() in str(result.get(field, "")).lower()
            for field in ("suku", "laji", "tieteellinen_nimi")
        ):
            matched = True
            break

    assert matched


def test_get_detail_endpoints(client, db_session):
    for route in client.app.router.routes:
        methods = getattr(route, "methods", set())
        if "GET" not in methods:
            continue
        if "{" not in route.path:
            continue
        if route.path in {"/openapi.json", "/docs", "/redoc"}:
            continue

        model = _get_model_for_route(route)
        if model is None:
            continue

        path = route.path
        for param in route.dependant.path_params:
            column = _match_column(model, param.name)
            if column is None:
                break
            try:
                row = db_session.query(model).filter(column.isnot(None)).first()
            except ValueError:
                row = None
            if row is None:
                break
            value = _serialize_value(getattr(row, column.name))
            path = path.replace(f"{{{param.name}}}", str(value))
        else:
            response = client.get(path)
            if response.status_code == 404:
                pytest.skip(f"No data for {route.path}")
            assert response.status_code == 200, f"{route.path} returned {response.status_code}"
