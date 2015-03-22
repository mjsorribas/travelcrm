"""alter db

Revision ID: 3d21723b3954
Revises: 18572a9133a9
Create Date: 2015-03-15 18:52:07.475748

"""

# revision identifiers, used by Alembic.
revision = '3d21723b3954'
down_revision = '18572a9133a9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('apscheduler_jobs')
    op.drop_column('person', 'gender_1')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('gender_1', postgresql.ENUM(u'male', u'female', name='genders_enum'), autoincrement=False, nullable=True))
    op.create_table('apscheduler_jobs',
    sa.Column('id', sa.VARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'apscheduler_jobs_pkey')
    )
    ### end Alembic commands ###