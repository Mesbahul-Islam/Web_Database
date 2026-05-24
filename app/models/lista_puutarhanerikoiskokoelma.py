from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class ListaPuutarhanerikoiskokoelma(Base):
    # Botanical garden special collection list
    __tablename__ = 'lista_puutarhanerikoiskokoelma'
    # ID
    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Name
    nimi: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("''"))
