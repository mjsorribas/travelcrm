"""alter db

Revision ID: 4525b9c2d99f
Revises: 32f865aa2c94
Create Date: 2014-11-05 21:00:49.246599

"""

# revision identifiers, used by Alembic.
revision = '4525b9c2d99f'
down_revision = '32f865aa2c94'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suppplier_subaccount',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('subaccount_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subaccount_id'], ['subaccount.id'], name='fk_subaccount_id_supplier_subaccount', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], name='fk_supplier_id_supplier_subaccount', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('supplier_id', 'subaccount_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suppplier_subaccount')
    ### end Alembic commands ###
