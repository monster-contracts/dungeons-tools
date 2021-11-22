"""empty message

Revision ID: a8ab6c1a5199
Revises: 9b3e5901e440
Create Date: 2021-11-22 16:16:16.632073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ab6c1a5199'
down_revision = '9b3e5901e440'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rarity_nft_holder', sa.Column('summoner_class', sa.String(length=10), nullable=True))
    op.add_column('rarity_nft_holder', sa.Column('summoner_level', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rarity_nft_holder', 'summoner_level')
    op.drop_column('rarity_nft_holder', 'summoner_class')
    # ### end Alembic commands ###