"""different states for admin."""
from aiogram.filters.state import State, StatesGroup


class Admin(StatesGroup):
    """state group for menu."""

    main = State()


class AddProduct(StatesGroup):
    """state group for menu."""

    get_file = State()
    get_city = State()
    get_address = State()
    get_product_name = State()
    get_product_description = State()
    get_product_price = State()
    confirm = State()
