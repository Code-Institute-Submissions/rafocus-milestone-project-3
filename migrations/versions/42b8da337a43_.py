"""empty message

Revision ID: 42b8da337a43
Revises: e810d70fc102
Create Date: 2019-07-29 13:56:13.543254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b8da337a43'
down_revision = 'e810d70fc102'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_diet',
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('diet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['diet_id'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['diet.id'], )
    )
    op.drop_column('recipe', 'requirement')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('requirement', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_table('recipe_diet')
    op.drop_table('diet')
    # ### end Alembic commands ###
