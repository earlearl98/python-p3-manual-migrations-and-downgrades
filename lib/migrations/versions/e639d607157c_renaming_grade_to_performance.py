"""Renaming grade to performance

Revision ID: e639d607157c
Revises: 35561fb94ee6
Create Date: 2023-12-06 17:50:25.774629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e639d607157c'
down_revision = '35561fb94ee6'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.rename_table('grade', 'performance')


def downgrade() -> None:
    op.rename_table('performance','grade' )   