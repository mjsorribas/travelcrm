"""alter db

Revision ID: 542af389e25e
Revises: 24298b9e6a3e
Create Date: 2015-04-25 15:15:11.741685

"""

# revision identifiers, used by Alembic.
revision = '542af389e25e'
down_revision = '24298b9e6a3e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], name='fk_resource_id_transport', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='unique_idx_name_transport')
    )
    op.create_table('tour',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('start_location_id', sa.Integer(), nullable=False),
    sa.Column('end_location_id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('accomodation_id', sa.Integer(), nullable=True),
    sa.Column('foodcat_id', sa.Integer(), nullable=True),
    sa.Column('roomcat_id', sa.Integer(), nullable=True),
    sa.Column('adults', sa.Integer(), nullable=False),
    sa.Column('children', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('descr', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['accomodation_id'], ['accomodation.id'], name='fk_accomodation_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['end_location_id'], ['location.id'], name='fk_end_location_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['foodcat_id'], ['foodcat.id'], name='fk_foodcat_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotel.id'], name='fk_hotel_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], name='fk_location_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], name='fk_resource_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['roomcat_id'], ['roomcat.id'], name='fk_roomcat_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['start_location_id'], ['location.id'], name='fk_start_location_id_tour', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tour_order_item',
    sa.Column('order_item_id', sa.Integer(), nullable=False),
    sa.Column('tour_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_item_id'], ['order_item.id'], name='fk_order_item_id_tour_order_item', onupdate='cascade', ondelete='restrict'),
    sa.ForeignKeyConstraint(['tour_id'], ['tour.id'], name='fk_tour_id_tour_order_item', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('order_item_id', 'tour_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tour_order_item')
    op.drop_table('tour')
    op.drop_table('transport')
    ### end Alembic commands ###