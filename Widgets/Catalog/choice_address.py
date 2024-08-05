"""getter for city name."""
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Select, Column, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Catalog, Basket
import operator

from Api.DB import get_addreses

from config import KEYBOARD


async def getter_addresses(dialog_manager: DialogManager, **kwargs):
    """Getter all addresses from db by city id."""
    city_id = dialog_manager.dialog_data["city_id"]
    addresses = await get_addreses(city_id)
    return {
        "addresses": addresses,
        "count": len(addresses)
    }


async def choice_address_handler(
        callback: CallbackQuery,
        widget,
        manager: DialogManager,
        item_id: str
):
    """Handle to save choosen address by city_id."""
    manager.dialog_data["address_id"] = item_id
    await manager.switch_to(state=Catalog.choice_product)


window = Window(
    Const("Выберите адрес:"),
    Column(
        Select(
            Format("{item[0]}"),
            id="address_select",
            item_id_getter=operator.itemgetter(1),
            items="addresses",
            on_click=choice_address_handler,
        ),
    ),
    SwitchTo(Const("‹ Назад"), id="back_to_choice_city", state=Catalog.choice_city),
    Start(Const("🛒 Перейти к корзине"), id="to_basket", state=Basket.main),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    markup_factory=KEYBOARD,
    getter=getter_addresses,
    state=Catalog.choice_address,
)
