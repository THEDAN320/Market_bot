"""getter for city name."""
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Select, Column, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Catalog, Basket
import operator

from Api.DB import get_products

from config import KEYBOARD


async def getter_products(dialog_manager: DialogManager, **kwargs):
    """Getter all products from db by address."""
    address_id = dialog_manager.dialog_data["address_id"]
    products = await get_products(address_id)
    return {
        "products": products,
        "count": len(products)
    }


async def choice_products_handler(
        callback: CallbackQuery,
        widget,
        manager: DialogManager,
        item_id: str
):
    """Handle to save choosen product by address_id."""
    manager.dialog_data["product_id"] = item_id
    await manager.switch_to(state=Catalog.product_info)


window = Window(
    Const("Выберите товар:"),
    Column(
        Select(
            Format("{item[0]}"),
            id="product_select",
            item_id_getter=operator.itemgetter(1),
            items="products",
            on_click=choice_products_handler,
        ),
    ),
    SwitchTo(Const("‹ Назад"), id="back_to_choice_address", state=Catalog.choice_address),
    Start(Const("🛒 Перейти к корзине"), id="to_basket", state=Basket.main),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    markup_factory=KEYBOARD,
    getter=getter_products,
    state=Catalog.choice_product,
)
