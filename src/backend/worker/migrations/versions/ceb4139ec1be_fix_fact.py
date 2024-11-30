"""fix_fact

Revision ID: ceb4139ec1be
Revises: 7623eafc6547
Create Date: 2024-11-30 17:23:35.391814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceb4139ec1be'
down_revision: Union[str, None] = '7623eafc6547'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fact_credit_sum_key', 'fact', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('fact_credit_sum_key', 'fact', ['credit_sum'])
    # ### end Alembic commands ###