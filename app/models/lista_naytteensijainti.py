from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaNaytteensijainti(Base):
    # Specimen location list
    __tablename__ = 'lista_naytteensijainti'
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Code
    koodi: Mapped[Optional[str]] = mapped_column(String(255))
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
