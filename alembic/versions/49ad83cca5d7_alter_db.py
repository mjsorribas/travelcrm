"""alter db

Revision ID: 49ad83cca5d7
Revises: 2160db5051a7
Create Date: 2015-07-18 11:54:18.340445

"""

# revision identifiers, used by Alembic.
revision = '49ad83cca5d7'
down_revision = '2160db5051a7'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], name='fk_resource_id_person_category', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='unique_idx_name_person_category')
    )
    op.drop_table('apscheduler_jobs')
    op.add_column('person', sa.Column('person_category_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_person_category_id_person', 'person', 'person_category', ['person_category_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_person_category_id_person', 'person', type_='foreignkey')
    op.drop_column('person', 'person_category_id')
    op.create_table('apscheduler_jobs',
    sa.Column('id', sa.VARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'apscheduler_jobs_pkey')
    )
    op.drop_table('person_category')
    ### end Alembic commands ###
