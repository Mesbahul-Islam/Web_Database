"""Migrate toimenpide uus_pvm to timestamps

Revision ID: 505937b598bc
Revises: ff5a2231b038
Create Date: 2026-06-22 23:29:21.400133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '505937b598bc'
down_revision: Union[str, Sequence[str], None] = 'ff5a2231b038'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    import datetime
    bind = op.get_bind()
    metadata = sa.MetaData()
    
    # We define only the required columns locally so this migration remains independent
    toimenpide = sa.Table(
        'toimenpide', metadata,
        sa.Column('toimenpide_nro', sa.Integer, primary_key=True),
        sa.Column('uus_pvm', sa.String(255)),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
    )

    query = toimenpide.select().where(toimenpide.c.uus_pvm.isnot(None))
    results = bind.execute(query).fetchall()

    for row in results:
        mapping = row._mapping
        raw_date = str(mapping["uus_pvm"]).strip()
        if not raw_date or raw_date == "0000-00-00" or raw_date == "0" or raw_date == "None":
            continue
            
        parsed_date = None
        try:
            parsed_date = datetime.datetime.fromisoformat(raw_date)
        except ValueError:
            if len(raw_date) == 4 and raw_date.isdigit():
                try:
                    parsed_date = datetime.datetime(int(raw_date), 1, 1)
                except ValueError:
                    pass
                    
        if parsed_date:
            update_stmt = (
                toimenpide.update()
                .where(toimenpide.c.toimenpide_nro == mapping["toimenpide_nro"])
                .values(created_at=parsed_date, updated_at=parsed_date)
            )
            bind.execute(update_stmt)


def downgrade() -> None:
    """Downgrade schema."""
    pass
