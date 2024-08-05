"""different states for default users."""
from aiogram.filters.state import State, StatesGroup


class Menu(StatesGroup):
    """state group for menu."""

    main = State()
    contacts = State()
    instruction = State()


class Basket(StatesGroup):
    """state group for basket."""

    main = State()
    pay = State()
    product_info = State()


class Catalog(StatesGroup):
    """state group for catalog."""

    choice_city = State()
    choice_address = State()
    choice_product = State()
    product_info = State()
