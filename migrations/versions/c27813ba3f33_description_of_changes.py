"""Description of changes

Revision ID: c27813ba3f33
Revises: 44ea7ced9915
Create Date: 2024-12-22 12:09:52.161575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c27813ba3f33'
down_revision = '44ea7ced9915'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Invoice',
    sa.Column('Invoice_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('Invoice_id')
    )
    op.create_table('User',
    sa.Column('userId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userName', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('role', sa.Text(), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('userId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User')
    op.drop_table('Invoice')
    # ### end Alembic commands ###
