"""different states for default users."""
from aiogram.filters.state import State, StatesGroup


class Menu(StatesGroup):
    """state group for menu."""

    main = State()
    comments = State()
    contacts = State()
    instruction = State()


class Basket(StatesGroup):
    """state group for basket."""

    main = State()


class Catalog(StatesGroup):
    """state group for catalog."""

    main = State()
