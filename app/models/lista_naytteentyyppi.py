from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaNaytteentyyppi(Base):
    # Specimen type list
    __tablename__ = 'lista_naytteentyyppi'
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Code
    koodi: Mapped[Optional[str]] = mapped_column(String(255))
