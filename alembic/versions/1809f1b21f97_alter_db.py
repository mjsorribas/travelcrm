"""alter db

Revision ID: 1809f1b21f97
Revises: None
Create Date: 2015-03-29 16:02:55.849843

"""

# revision identifiers, used by Alembic.
revision = '1809f1b21f97'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(precision=16, scale=2), nullable=True),
    sa.Column('descr', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], name='fk_currency_id_offer', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], name='fk_resource_id_offer', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], name='fk_service_id_offer', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=True),
    sa.Column('price_from', sa.Numeric(precision=16, scale=2), nullable=True),
    sa.Column('price_to', sa.Numeric(precision=16, scale=2), nullable=True),
    sa.Column('descr', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], name='fk_currency_id_wish', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], name='fk_resource_id_wish', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], name='fk_service_id_wish', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lead_offer',
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('offer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lead_id'], ['lead.id'], name='fk_lead_id_lead_offer', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['offer_id'], ['offer.id'], name='fk_offer_item_id_lead_offer', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('lead_id', 'offer_id')
    )
    op.create_table('lead_wish',
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('wish_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lead_id'], ['lead.id'], name='fk_lead_id_lead_wish', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['wish_id'], ['wish.id'], name='fk_wish_id_lead_wish', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('lead_id', 'wish_id')
    )
    op.drop_table('apscheduler_jobs')
    op.drop_table('offer_item')
    op.drop_table('wish_item')
    op.add_column(u'company', sa.Column('email', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'company', 'email')
    op.create_table('wish_item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('resource_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('currency_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price_from', sa.NUMERIC(precision=16, scale=2), autoincrement=False, nullable=True),
    sa.Column('price_to', sa.NUMERIC(precision=16, scale=2), autoincrement=False, nullable=True),
    sa.Column('descr', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['currency_id'], [u'currency.id'], name=u'fk_currency_id_wish_item', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.ForeignKeyConstraint(['resource_id'], [u'resource.id'], name=u'fk_resource_id_wish_item', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.ForeignKeyConstraint(['service_id'], [u'service.id'], name=u'fk_service_id_wish_item', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'wish_item_pkey')
    )
    op.create_table('offer_item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('resource_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('currency_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.NUMERIC(precision=16, scale=2), autoincrement=False, nullable=True),
    sa.Column('descr', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['currency_id'], [u'currency.id'], name=u'fk_currency_id_offer_item', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.ForeignKeyConstraint(['resource_id'], [u'resource.id'], name=u'fk_resource_id_offer_item', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.ForeignKeyConstraint(['service_id'], [u'service.id'], name=u'fk_service_id_offer_item', onupdate=u'CASCADE', ondelete=u'RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=u'offer_item_pkey')
    )
    op.create_table('apscheduler_jobs',
    sa.Column('id', sa.VARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'apscheduler_jobs_pkey')
    )
    op.drop_table('lead_wish')
    op.drop_table('lead_offer')
    op.drop_table('wish')
    op.drop_table('offer')
    ### end Alembic commands ###