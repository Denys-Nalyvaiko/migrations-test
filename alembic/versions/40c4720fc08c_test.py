"""test

Revision ID: 40c4720fc08c
Revises: 3a3a3b7792b3
Create Date: 2024-04-18 02:25:51.059825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40c4720fc08c'
down_revision: Union[str, None] = '3a3a3b7792b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
