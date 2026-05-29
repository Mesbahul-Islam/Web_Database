from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Huomoita(Base):
    # Notes (typo variant)
    __tablename__ = 'huomoita'
    # Panel
    paneeli: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("''"))
    # Note
    huom: Mapped[Optional[str]] = mapped_column(Text)
