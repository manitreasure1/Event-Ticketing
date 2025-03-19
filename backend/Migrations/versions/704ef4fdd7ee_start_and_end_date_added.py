"""start and end date added

Revision ID: 704ef4fdd7ee
Revises: 
Create Date: 2025-03-18 19:23:49.481735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '704ef4fdd7ee'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('event', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.add_column('event', sa.Column('end_date', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('event', 'start_date')
    op.drop_column('event', 'end_date')
    
