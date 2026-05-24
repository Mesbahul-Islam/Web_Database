from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Koe(Base):
    # Experimental or test table
    __tablename__ = 'koe'
    # ID
    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Value
    i: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Text
    t: Mapped[Optional[str]] = mapped_column(String(255))
