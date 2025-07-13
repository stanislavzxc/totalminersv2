"""create_initial_tables

Revision ID: 2025_02_05_initial
Revises: 
Create Date: 2025-02-05 12:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5775661d755b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'business',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('miner1', sa.String(), nullable=True),
        sa.Column('count1', sa.Integer(), nullable=True),
        sa.Column('hosting_discount1', sa.Integer(), nullable=True),
        sa.Column('miner2', sa.String(), nullable=True),
        sa.Column('count2', sa.Integer(), nullable=True),
        sa.Column('hosting_discount2', sa.Integer(), nullable=True),
        sa.Column('miner3', sa.String(), nullable=True),
        sa.Column('count3', sa.Integer(), nullable=True),
        sa.Column('hosting_discount3', sa.Integer(), nullable=True),
    )

    op.create_table(
        'balances',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('value', sa.BigInteger(), nullable=True),
        sa.Column('date', sa.String(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'billings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('type', sa.String(length=32), nullable=True),
        sa.Column('state', sa.String(length=32), nullable=True),
        sa.Column('value', sa.BigInteger(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('payment_type', sa.String(length=32), nullable=True),
        sa.Column('payment_data', sa.String(length=512), nullable=True),
        sa.Column('currency', sa.String(length=32), nullable=True),
        sa.Column('value_usd', sa.BigInteger(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
    )

    op.create_table(
        'billings_buy_requests',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('billing_id', sa.Integer(), nullable=True),
        sa.Column('buy_request_id', sa.Integer(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'billings_payments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('billing_id', sa.Integer(), nullable=True),
        sa.Column('payment_id', sa.Integer(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'buy_request_miner_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('buy_request_id', sa.Integer(), nullable=True),
        sa.Column('miner_item_id', sa.Integer(), nullable=True),
        sa.Column('count', sa.Integer(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'buy_requests',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('state', sa.String(length=32), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'countries',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('short_code', sa.String(), nullable=True),
    )

    op.create_table(
        'employees',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'feedbacks',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('phone', sa.String(length=32), nullable=True),
        sa.Column('state', sa.String(length=16), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'images',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('path', sa.String(length=256), nullable=True),
        sa.Column('filename', sa.String(length=128), nullable=True),
        sa.Column('extension', sa.String(length=8), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'markets_carts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('miner_item_id', sa.Integer(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('count', sa.Integer(), nullable=True),
    )

    op.create_table(
        'messages',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('content', sa.String(), nullable=True),
        sa.Column('ticket_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('sender', sa.String(length=32), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
    )

    op.create_table(
        'miner_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('hash_rate', sa.BigInteger(), nullable=True),
        sa.Column('energy_consumption', sa.Integer(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('is_hidden', sa.Boolean(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.Column('priority', sa.Integer(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('discount_count', sa.Integer(), nullable=True),
        sa.Column('discount_value', sa.Integer(), nullable=True),
    )

    op.create_table(
        'miner_items_categories',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('is_hidden', sa.Boolean(), nullable=True),
        sa.Column('priority', sa.Integer(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'payments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('type', sa.String(length=32), nullable=True),
        sa.Column('currency', sa.String(length=8), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('value', sa.BigInteger(), nullable=True),
        sa.Column('date', sa.String(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('date_time', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'payments_sites',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('payment_id', sa.Integer(), nullable=True),
        sa.Column('site_id', sa.String(length=128), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('hash_rate', sa.BigInteger(), nullable=True),
    )

    op.create_table(
        'purchases_records',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('date', sa.DateTime(), nullable=True),
        sa.Column('amount', sa.Integer(), nullable=True),
    )

    op.create_table(
        'resets_passwords_requests',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('expired', sa.Boolean(), nullable=True),
    )

    op.create_table(
        'settings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('key', sa.String(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
    )

    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('is_open', sa.Boolean(), nullable=True),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('firstname', sa.String(), nullable=True),
        sa.Column('lastname', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('telegram', sa.String(), nullable=True),
        sa.Column('country', sa.String(), nullable=True),
        sa.Column('address', sa.String(), nullable=True),
        sa.Column('inn', sa.String(), nullable=True),
        sa.Column('profile_type', sa.String(), nullable=True),
        sa.Column('last_totp', sa.String(), nullable=True),
        sa.Column('totp_sent', sa.DateTime(), nullable=True),
        sa.Column('wallet', sa.String(), nullable=True),
        sa.Column('mfa_key', sa.String(), nullable=True),
        sa.Column('mfa_enabled', sa.Boolean(), nullable=True),
        sa.Column('miner_name', sa.String(), nullable=True),
        sa.Column('miner_id', sa.String(), nullable=True),
        sa.Column('wallet_id', sa.String(), nullable=True),
        sa.Column('access_allowed', sa.Boolean(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.Column('lang', sa.String(length=4), nullable=True),
    )

    op.create_table(
        'workers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('miner_item_id', sa.Integer(), nullable=True),
        sa.Column('id_str', sa.String(length=64), nullable=True),
        sa.Column('name', sa.String(length=128), nullable=True),
        sa.Column('behavior', sa.String(length=32), nullable=True),
        sa.Column('hidden', sa.Boolean(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('workers')
    op.drop_table('users')
    op.drop_table('tickets')
    op.drop_table('settings')
    op.drop_table('resets_passwords_requests')
    op.drop_table('purchases_records')
    op.drop_table('payments_sites')
    op.drop_table('payments')
    op.drop_table('miner_items_categories')
    op.drop_table('miner_items')
    op.drop_table('messages')
    op.drop_table('markets_carts')
    op.drop_table('images')
    op.drop_table('feedbacks')
    op.drop_table('employees')
    op.drop_table('countries')
    op.drop_table('buy_requests')
    op.drop_table('buy_request_miner_items')
    op.drop_table('billings_payments')
    op.drop_table('billings_buy_requests')
    op.drop_table('billings')
    op.drop_table('balances')
    op.drop_table('business')
