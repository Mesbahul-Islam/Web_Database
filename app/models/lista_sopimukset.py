from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaSopimukset(Base):
    # Agreements list
    __tablename__ = 'lista_sopimukset'
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
