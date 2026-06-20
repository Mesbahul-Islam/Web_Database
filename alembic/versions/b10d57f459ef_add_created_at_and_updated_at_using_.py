"""Add created_at and updated_at using batch mode

Revision ID: b10d57f459ef
Revises: f8985dffebf3
Create Date: 2026-06-20 02:06:52.987920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b10d57f459ef'
down_revision: Union[str, Sequence[str], None] = 'f8985dffebf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    tables = [
        'alkuperaa_koskevat_tiedot', 'hankintatiedot', 'kasvatustietoja', 
        'lahettaja', 'maaritysmerkinta', 'naytetietoja', 'osastopaikka', 
        'puutarhassa_viljelyn_tarkoitus', 'taksoni', 'toimenpide'
    ]
    for table in tables:
        op.add_column(table, sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=True))
        op.add_column(table, sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), nullable=True))

def downgrade() -> None:
    tables = [
        'alkuperaa_koskevat_tiedot', 'hankintatiedot', 'kasvatustietoja', 
        'lahettaja', 'maaritysmerkinta', 'naytetietoja', 'osastopaikka', 
        'puutarhassa_viljelyn_tarkoitus', 'taksoni', 'toimenpide'
    ]
    for table in tables:
        op.drop_column(table, 'updated_at')
        op.drop_column(table, 'created_at')

