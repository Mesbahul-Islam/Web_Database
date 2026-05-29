from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Maaritysmerkinta(Base):
    # Identification mark record
    __tablename__ = 'maaritysmerkinta'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='maaritysmerkinta_ibfk_1'), Index('IDX_Maaritysmerkinta1', 'hankintaID'))
    # Maaritysnro
    maaritysnro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Identification date
    maarityspvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Identifier
    maarittaja: Mapped[Optional[str]] = mapped_column(String(255))
    # Identification level
    maaritystaso: Mapped[Optional[str]] = mapped_column(String(255))
    # Remark
    huomautus: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition ID
    hankintaID: Mapped[Optional[int]] = mapped_column(Integer)
    # Section
    osasto: Mapped[Optional[str]] = mapped_column(String(255))
    # Paikka
    paikka: Mapped[Optional[str]] = mapped_column(String(255))
    # Old taxon
    vanhataksoni: Mapped[Optional[str]] = mapped_column(String(255))
    # New taxon
    uusitaksoni: Mapped[Optional[str]] = mapped_column(String(255))
    # New identification date
    uus_maarityspvm: Mapped[Optional[datetime.date]] = mapped_column(Date)
    # Acquisition data
    hankintatiedot: Mapped[Optional['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='maaritysmerkinta')
