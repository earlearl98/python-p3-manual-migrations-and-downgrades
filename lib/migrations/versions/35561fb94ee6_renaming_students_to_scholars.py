"""Renaming students to scholars

Revision ID: 35561fb94ee6
Revises: 791279dd0760
Create Date: 2023-12-06 17:33:14.410502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35561fb94ee6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')




# def upgrade() -> None:
#     op.rename_table('grade', 'performance')


# def downgrade() -> None:
#     op.rename_table('performance','grade' )    

    
    



