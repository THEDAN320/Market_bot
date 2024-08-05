"""getter for city name."""
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Select, Column
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Catalog, Basket
import operator

from Api.DB import get_cities

from config import KEYBOARD


async def getter_cities(**kwargs):
    """Getter all cities from db."""
    cities = await get_cities()
    return {
        "cities": cities,
        "count": len(cities)
    }


async def choice_city_handler(
        callback: CallbackQuery,
        widget,
        manager: DialogManager,
        item_id: str
):
    """Handle to save choosen city."""
    manager.dialog_data["city_id"] = item_id
    await manager.switch_to(state=Catalog.choice_address)


window = Window(
    Const("Выберите город:"),
    Column(
        Select(
            Format("{item[0]}"),
            id="city_select",
            item_id_getter=operator.itemgetter(1),
            items="cities",
            on_click=choice_city_handler,
        ),
    ),
    Start(Const("🛒 Перейти к корзине"), id="to_basket", state=Basket.main),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    markup_factory=KEYBOARD,
    getter=getter_cities,
    state=Catalog.choice_city,
)
