"""new ralationship

Revision ID: acb1a7d7fd64
Revises: 13da58143fef
Create Date: 2023-01-26 15:06:41.472126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb1a7d7fd64'
down_revision = '13da58143fef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('movies_actors',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('actor_id', 'film_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies_actors')
    op.drop_table('users')
    # ### end Alembic commands ###
