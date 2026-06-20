from app.database import Base
import datetime
from typing import Optional
from sqlalchemy import DateTime, TypeDecorator, String
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )


class SafeDate(TypeDecorator):
    """
    A custom SQLAlchemy Date type decorator that safely handles malformed date data
    (such as integer years, empty strings, or invalid strings) stored in SQLite columns,
    preventing conversion errors on deserialization.
    """
    impl = String
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, datetime.date):
            return value.isoformat()
        return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, datetime.date):
            return value
        value_str = str(value).strip()
        if not value_str or value_str in ("0", "0000-00-00"):
            return None
        try:
            return datetime.date.fromisoformat(value_str)
        except ValueError:
            # Fallback for year-only formats (e.g., "2005")
            if len(value_str) == 4 and value_str.isdigit():
                try:
                    return datetime.date(int(value_str), 1, 1)
                except ValueError:
                    return None
            return None


__all__ = ["Base", "TimestampMixin", "SafeDate"]

