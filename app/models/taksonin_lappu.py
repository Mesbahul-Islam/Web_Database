from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class TaksoninLappu(Base):
    # Taxon label
    __tablename__ = 'taksonin_lappu'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='taksonin_lappu_ibfk_1'), Index('IDX_Taksonin_lappu1', 'taksonin_nro'))
    # Label number
    Lappu_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Label text
    Lappu_teksti: Mapped[Optional[str]] = mapped_column(Text)
    # Taxon number
    taksonin_nro: Mapped[Optional[int]] = mapped_column(Integer)
    # Taxon
    taksoni: Mapped[Optional['Taksoni']] = relationship('Taksoni', back_populates='taksonin_lappu')
