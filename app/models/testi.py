from .base import Base, SafeDate
from typing import Optional
import datetime
from sqlalchemy import Column, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Testi(Base):
    # Test table
    __tablename__ = 'testi'
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Date
    pvm: Mapped[Optional[str]] = mapped_column(String(255))
    # New date
    uuspvm: Mapped[Optional[datetime.date]] = mapped_column(SafeDate)

