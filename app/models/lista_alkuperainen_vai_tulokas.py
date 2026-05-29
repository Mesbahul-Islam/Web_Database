from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaAlkuperainenVaiTulokas(Base):
    # Native or introduced plant list
    __tablename__ = 'lista_alkuperainen_vai_tulokas'
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(100))
