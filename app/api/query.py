from datetime import datetime
from typing import Any

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
    
    for key, value in params.multi_items():  # alue: area
        if key in {"skip", "limit"}:
            continue
        if not hasattr(model, key):
            continue
        column = getattr(model, key)
        query = query.filter(column == _coerce_value(column, value))  # alue: area
    return query
