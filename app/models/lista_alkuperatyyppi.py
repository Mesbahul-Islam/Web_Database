from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaAlkuperatyyppi(Base):
    # Origin type list
    __tablename__ = 'lista_alkuperatyyppi'
    # Name
    nimi: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("''"))
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
