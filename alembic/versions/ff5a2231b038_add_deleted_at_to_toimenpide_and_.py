"""Add deleted_at to toimenpide and tarkastusmerkinta

Revision ID: ff5a2231b038
Revises: 99edebf4dbde
Create Date: 2026-06-22 23:10:29.183431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import app.models.base


# revision identifiers, used by Alembic.
revision: str = 'ff5a2231b038'
down_revision: Union[str, Sequence[str], None] = '99edebf4dbde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('tarkastusmerkinta', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('toimenpide', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted_at', sa.DateTime(), nullable=True))

def downgrade() -> None:
    with op.batch_alter_table('toimenpide', schema=None) as batch_op:
        batch_op.drop_column('deleted_at')

    with op.batch_alter_table('tarkastusmerkinta', schema=None) as batch_op:
        batch_op.drop_column('deleted_at')
    # ### end Alembic commands ###
