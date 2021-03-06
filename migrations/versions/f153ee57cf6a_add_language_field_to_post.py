"""add language field to Post

Revision ID: f153ee57cf6a
Revises: b32ab0058fe7
Create Date: 2018-06-24 17:03:06.114831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f153ee57cf6a'
down_revision = 'b32ab0058fe7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
