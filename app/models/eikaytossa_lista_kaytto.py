from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class EikaytossaListaKaytto(Base):
    # Obsolete usage list
    __tablename__ = 'eikaytossa_lista_kaytto'
    # ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
