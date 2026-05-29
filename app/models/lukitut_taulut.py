from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class LukitutTaulut(Base):
    # Locked tables
    __tablename__ = 'lukitut_taulut'
    __table_args__ = (Index('avainkentta', 'avainkentta', unique=True),)
    # User identifier
    kayttajan_tunnus: Mapped[str] = mapped_column(String(100), primary_key=True, server_default=text("''"))
    # Table name
    taulun_nimi: Mapped[Optional[str]] = mapped_column(String(100))
    # Key field
    avainkentta: Mapped[Optional[str]] = mapped_column(String(100))
