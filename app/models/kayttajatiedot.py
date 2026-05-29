from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Kayttajatiedot(Base):
    # User data
    __tablename__ = 'kayttajatiedot'
    __table_args__ = (Index('kayttajan_tunnus', 'kayttajan_tunnus', unique=True),)
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # User identifier
    kayttajan_tunnus: Mapped[Optional[str]] = mapped_column(String(100))
    # User name
    kayttajan_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # User level
    kayttajan_taso: Mapped[Optional[int]] = mapped_column(Integer)
    # Additional information
    lisatietoja: Mapped[Optional[str]] = mapped_column(String(255))
