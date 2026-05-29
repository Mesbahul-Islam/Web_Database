from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Hyotykaytto(Base):
    # Utility use
    __tablename__ = 'hyotykaytto'
    # ID
    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Name
    NIMI: Mapped[Optional[str]] = mapped_column(String(255))
    # Code
    KOODI: Mapped[Optional[str]] = mapped_column(String(100))
    # Number
    NUMERO: Mapped[Optional[str]] = mapped_column(String(100))
