"""empty message

Revision ID: 85de1b468c02
Revises: f309dca37c7c
Create Date: 2023-02-16 18:16:27.291376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85de1b468c02'
down_revision = 'f309dca37c7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('balance', sa.Integer(), nullable=True))
    op.drop_column('account', 'amount')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('amount', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('account', 'balance')
    # ### end Alembic commands ###
