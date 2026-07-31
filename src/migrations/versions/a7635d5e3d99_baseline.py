"""baseline

Revision ID: a7635d5e3d99
Revises: 3263133c6314
Create Date: 2026-07-29 08:20:05.629675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7635d5e3d99'
down_revision: Union[str, Sequence[str], None] = '3263133c6314'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
