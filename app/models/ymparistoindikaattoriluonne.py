from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Ymparistoindikaattoriluonne(Base):
    # Environmental indicator characteristic
    __tablename__ = 'ymparistoindikaattoriluonne'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='ymparistoindikaattoriluonne_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='ymparistoindikaattoriluonne_ibfk_2'), Index('IDX_Ymparistoindikaattoriluonne1', 'taksonin_nro'), Index('IDX_Ymparistoindikaattoriluonne2', 'viitenro'))
    # Indicator number
    indikaattorin_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Environmental indicator characteristic
    ymparistoindikaattoriluonne: Mapped[Optional[str]] = mapped_column(String(255))
    # Environmental indicator explanation
    ymparistoindikaattorin_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='ymparistoindikaattoriluonne')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='ymparistoindikaattoriluonne')
