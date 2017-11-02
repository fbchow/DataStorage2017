"""empty message

Revision ID: ede54e6a40c9
Revises: 
Create Date: 2017-11-01 20:57:51.668682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ede54e6a40c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transportation',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('id2', sa.Integer(), nullable=True),
    sa.Column('disp_label', sa.String(length=100), nullable=True),
    sa.Column('HC01_EST_VC01', sa.Integer(), nullable=True),
    sa.Column('HC01_MOE_VC01', sa.Integer(), nullable=True),
    sa.Column('HC02_EST_VC01', sa.Integer(), nullable=True),
    sa.Column('HC02_MOE_VC01', sa.Integer(), nullable=True),
    sa.Column('HC03_EST_VC01', sa.Integer(), nullable=True),
    sa.Column('HC03_MOE_VC01', sa.Integer(), nullable=True),
    sa.Column('HC01_EST_VC03', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC03', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC03', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC03', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC03', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC03', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC04', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC04', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC04', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC04', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC04', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC04', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC05', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC05', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC05', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC05', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC05', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC05', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC06', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC06', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC06', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC06', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC06', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC06', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC07', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC07', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC07', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC07', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC07', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC07', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC08', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC08', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC08', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC08', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC08', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC08', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC09', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC09', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC09', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC09', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC09', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC09', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC10', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC10', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC10', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC10', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC10', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC10', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC11', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC11', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC11', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC11', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC11', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC11', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC12', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC12', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC12', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC12', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC12', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC12', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC13', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC13', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC13', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC13', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC13', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC13', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC14', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC14', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC14', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC14', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC14', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC14', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC17', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC17', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC17', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC17', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC17', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC17', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC18', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC18', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC18', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC18', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC18', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC18', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC19', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC19', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC19', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC19', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC19', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC19', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC20', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC20', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC20', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC20', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC20', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC20', sa.Float(), nullable=True),
    sa.Column('HC01_EST_VC22', sa.Float(), nullable=True),
    sa.Column('HC01_MOE_VC22', sa.Float(), nullable=True),
    sa.Column('HC02_EST_VC22', sa.Float(), nullable=True),
    sa.Column('HC02_MOE_VC22', sa.Float(), nullable=True),
    sa.Column('HC03_EST_VC22', sa.Float(), nullable=True),
    sa.Column('HC03_MOE_VC22', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transportation')
    # ### end Alembic commands ###