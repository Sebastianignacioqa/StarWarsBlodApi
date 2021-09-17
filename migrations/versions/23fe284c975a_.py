"""empty message

Revision ID: 23fe284c975a
Revises: b81b3baa6838
Create Date: 2021-09-17 20:53:08.542468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23fe284c975a'
down_revision = 'b81b3baa6838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_name', sa.String(length=50), nullable=False))
    op.add_column('user', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=50), nullable=False))
    op.drop_column('user', 'name')
    op.drop_column('user', 'isActive')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('isActive', sa.BOOLEAN(), nullable=True))
    op.add_column('user', sa.Column('name', sa.VARCHAR(length=50), nullable=False))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'user_name')
    # ### end Alembic commands ###
