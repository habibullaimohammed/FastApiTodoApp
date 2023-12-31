"""create address table

Revision ID: bfa8deacb8fa
Revises: 662a06e5c895
Create Date: 2023-08-28 01:06:35.979283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'bfa8deacb8fa'
down_revision: Union[str, None] = '662a06e5c895'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address1", sa.String, nullable=False),
                    sa.Column("address2", sa.String, nullable=False),
                    sa.Column("city", sa.String, nullable=False),
                    sa.Column("state", sa.String, nullable=False),
                    sa.Column("country", sa.String, nullable=False),
                    sa.Column("postalcode", sa.String, nullable=False),
                    )


def downgrade() -> None:
    op.drop_table("address")
