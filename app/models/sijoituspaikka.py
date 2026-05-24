from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Sijoituspaikka(Base):
    # Placement location
    __tablename__ = 'sijoituspaikka'
    __table_args__ = (ForeignKeyConstraint(['osaston_numero'], ['osastopaikka.osaston_numero'], name='sijoituspaikka_ibfk_1'), Index('IDX_Sijoituspaikka1', 'osaston_numero'))
    # Placement location number
    sijoituspaikan_nro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Section number
    osaston_numero: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Placement date
    sijoituspvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Plot
    ruutu: Mapped[Optional[str]] = mapped_column(String(255))
    # Placement location name
    sijoituspaikan_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Plant status
    kasvin_status: Mapped[Optional[str]] = mapped_column(String(255))
    # Placement coordinates
    sijoituspaikan_koordinaatit: Mapped[Optional[str]] = mapped_column(String(255))
    # Placement old data
    sijoituspaikka_vanhat_tiedot: Mapped[Optional[str]] = mapped_column(String(255))
    # Plant remarks
    kasvin_huomautuksia: Mapped[Optional[str]] = mapped_column(Text)
    # Section location
    osastopaikka: Mapped['Osastopaikka'] = relationship('Osastopaikka', back_populates='sijoituspaikka')
    # Inspection record
    tarkastusmerkinta: Mapped[list['Tarkastusmerkinta']] = relationship('Tarkastusmerkinta', back_populates='sijoituspaikka')
