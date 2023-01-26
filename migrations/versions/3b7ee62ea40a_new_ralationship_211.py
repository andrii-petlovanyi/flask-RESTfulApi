"""new ralationship 211

Revision ID: 3b7ee62ea40a
Revises: 0929ffbae3a0
Create Date: 2023-01-26 16:36:41.400763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b7ee62ea40a'
down_revision = '0929ffbae3a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies_actors', schema=None) as batch_op:
        batch_op.alter_column('actor_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('film_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies_actors', schema=None) as batch_op:
        batch_op.alter_column('film_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('actor_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###