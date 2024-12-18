"""Create table

Revision ID: 44ea7ced9915
Revises: 
Create Date: 2024-12-17 20:07:11.483550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44ea7ced9915'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Inventory',
    sa.Column('SSR_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fab_Inventory_id', sa.Text(), nullable=False),
    sa.Column('fabricant', sa.Text(), nullable=False),
    sa.Column('fab_Inventory_name', sa.Text(), nullable=False),
    sa.Column('qunt', sa.Integer(), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('SSR_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Inventory')
    # ### end Alembic commands ###
