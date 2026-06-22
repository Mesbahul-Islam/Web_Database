from typing import Any

from fastapi import HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session


def _clean_payload(model: Any, payload: Any) -> dict[str, Any]:
    if isinstance(payload, BaseModel):
        payload = payload.model_dump(exclude_unset=True)

    if not isinstance(payload, dict):
        raise HTTPException(status_code=422, detail="Request body must be a JSON object")

    allowed_fields = {column.name for column in model.__table__.columns}
    return {key: value for key, value in payload.items() if key in allowed_fields}


async def _extract_payload(payload: Any) -> Any:
    if isinstance(payload, Request):
        return await payload.json()
    return payload


async def create_item(payload: Any, db: Session, model: Any):
    data = _clean_payload(model, await _extract_payload(payload))
    item = model(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


async def update_item(payload: Any, db: Session, model: Any, pk_field: str, pk_value: Any):
    item = db.query(model).filter(getattr(model, pk_field) == pk_value).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")

    data = _clean_payload(model, await _extract_payload(payload))
    for field, value in data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)
    return item


import datetime

async def delete_item(db: Session, model: Any, pk_field: str, pk_value: Any):
    item = db.query(model).filter(getattr(model, pk_field) == pk_value).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")

    if hasattr(item, "deleted_at"):
        item.deleted_at = datetime.datetime.now(datetime.timezone.utc)
    else:
        db.delete(item)
        
    db.commit()