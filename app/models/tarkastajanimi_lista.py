from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class TarkastajanimiLista(Base):
    # Inspector name list
    __tablename__ = 'tarkastajanimi_lista'
    # ID
    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Abbreviation
    lyhenne: Mapped[Optional[str]] = mapped_column(String(10))
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
