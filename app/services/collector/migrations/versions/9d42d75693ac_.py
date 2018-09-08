"""empty message

Revision ID: 9d42d75693ac
Revises: 
Create Date: 2018-09-08 16:24:50.962348

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9d42d75693ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('temperatures', sa.Column('LocalDateTime', sa.DateTime(), nullable=True))
    op.drop_column('temperatures', 'UTCDateTime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('temperatures', sa.Column('UTCDateTime', mysql.DATETIME(), nullable=True))
    op.drop_column('temperatures', 'LocalDateTime')
    # ### end Alembic commands ###