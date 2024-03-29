"""empty message

Revision ID: e810d70fc102
Revises: 08db2d27df57
Create Date: 2019-07-29 13:44:06.969639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e810d70fc102'
down_revision = '08db2d27df57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('cuisine', sa.String(length=100), nullable=False),
    sa.Column('ingredients', sa.Text(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('preparation', sa.Text(), nullable=False),
    sa.Column('requirement', sa.String(length=100), nullable=False),
    sa.Column('picture', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('recipe_diet')
    op.drop_table('diet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diet',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('diet_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='diet_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('recipe_diet',
    sa.Column('recipe_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('diet_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['diet.id'], name='recipe_diet_recipe_id_fkey')
    )
    op.drop_table('recipe')
    # ### end Alembic commands ###
