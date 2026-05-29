from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Huomioita(Base):
    # Notes or remarks
    __tablename__ = 'huomioita'
    # Panel
    paneeli: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("''"))
    # Note
    huom: Mapped[Optional[str]] = mapped_column(Text)
