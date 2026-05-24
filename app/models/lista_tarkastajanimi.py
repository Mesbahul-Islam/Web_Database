from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.mysql import INTEGER

from .base import Base


class ListaTarkastajanimi(Base):
    __table__ = Table(
        "lista_tarkastajanimi",
        Base.metadata,
        Column("id", INTEGER(11)),
        Column("nimi", String(255)),
        extend_existing=True,
    )
    # The source schema has no primary key, so we provide a composite
    # identity for ORM usage without implying a DB constraint.
    __mapper_args__ = {"primary_key": [__table__.c.id, __table__.c.nimi]}

