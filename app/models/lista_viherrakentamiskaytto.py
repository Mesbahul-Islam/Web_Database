from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaViherrakentamiskaytto(Base):
    # Green space use list
    __tablename__ = 'lista_viherrakentamiskaytto'
    # ID
    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Name
    NIMI: Mapped[Optional[str]] = mapped_column(String(255))
    # Code
    KOODI: Mapped[Optional[str]] = mapped_column(String(100))
