from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b61d4a7e841a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('products')
    has_category_id = any(column['name'] == 'category_id' for column in columns)

    if not has_category_id:
        op.add_column('products', sa.Column('category_id', sa.Integer(), nullable=True))

    has_created_at = any(column['name'] == 'created_at' for column in columns)

    if not has_created_at:
        op.add_column('products', sa.Column('created_at', sa.Date))

        op.create_table(
            'temp_products',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('created_at', sa.Date),
        )

        op.execute("INSERT INTO temp_products (id, created_at) SELECT id, DATE(created_at) FROM products")

        op.drop_column('products', 'created_at')

        op.alter_column('products', 'created_at', new_column_name='created_at')

    # ### end Alembic commands ###


def downgrade() -> None:
    op.alter_column('products', 'created_at', new_column_name='created_at')

    op.drop_table('temp_products')

    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('products')
    has_category_id = any(column['name'] == 'category_id' for column in columns)

    if has_category_id:
        op.drop_column('products', 'category_id')

