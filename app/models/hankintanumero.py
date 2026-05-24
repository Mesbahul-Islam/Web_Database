from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Hankintanumero(Base):
    # Acquisition number
    __tablename__ = 'hankintanumero'
    # Uusin Acquisition number
    uusin_hankintanumero: Mapped[str] = mapped_column(String(20), primary_key=True, server_default=text("''"))
