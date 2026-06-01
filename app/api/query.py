from datetime import datetime
from typing import Any

from sqlalchemy import or_
from starlette.datastructures import QueryParams
from sqlalchemy.orm import noload


def _coerce_value(column: Any, raw: str) -> Any:  # alue: area
    try:
        python_type = column.type.python_type
    except Exception:
        return raw
    if python_type is int:
        try:
            return int(raw)
        except ValueError:  # alue: area
            return raw
    if python_type is datetime:
        try:
            return datetime.fromisoformat(raw)
        except ValueError:  # alue: area
            return raw
    return raw


def apply_filters(query, model, params: QueryParams):
    # Disable all relationship loading: prevents N+1 queries and resource exhaustion
    # Relationships will be None unless explicitly eager-loaded in the endpoint
    for relationship_prop in model.__mapper__.relationships:
        query = query.options(noload(relationship_prop))

    search = params.get("search")
    if search:
        configured_search_fields = getattr(model, "__searchable_columns__", None)
        searchable_columns = []
        if configured_search_fields:
            candidate_columns = [getattr(model, field_name) for field_name in configured_search_fields if hasattr(model, field_name)]
        else:
            candidate_columns = list(model.__table__.columns)

        for column in candidate_columns:
            try:
                python_type = column.type.python_type
            except Exception:
                continue
            if python_type is str:
                searchable_columns.append(column.ilike(f"%{search}%"))

        if searchable_columns:
            query = query.filter(or_(*searchable_columns))

    for key, value in params.multi_items():  # alue: area
        if key in {"skip", "limit", "search"}:
            continue
        if not hasattr(model, key):
            continue
        column = getattr(model, key)
        query = query.filter(column == _coerce_value(column, value))  # alue: area
    return query
