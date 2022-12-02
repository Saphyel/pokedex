"""Added pokemon table"""
import sqlalchemy as sa

from alembic import op

revision = "9a589e04684b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "pokemon",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("abilities", sa.JSON(), nullable=True),
        sa.Column("captured", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("pokemon")
