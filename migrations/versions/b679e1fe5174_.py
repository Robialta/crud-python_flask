"""empty message

Revision ID: b679e1fe5174
Revises: ac3d61010e2d
Create Date: 2018-06-30 03:29:13.920629

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b679e1fe5174'
down_revision = 'ac3d61010e2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mahasiswa', 'nim',
               existing_type=mysql.VARCHAR(length=5),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mahasiswa', 'nim',
               existing_type=mysql.VARCHAR(length=5),
               nullable=True)
    # ### end Alembic commands ###
