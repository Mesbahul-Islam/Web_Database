from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaLisaystapa(Base):
    # Addition method list
    __tablename__ = 'lista_lisaystapa'
    # ID
    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Code
    koodi: Mapped[Optional[str]] = mapped_column(String(100))
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
