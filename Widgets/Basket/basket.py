"""getter for city name."""
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, DialogManager, Dialog, ShowMode
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Select, Column, Button
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Basket
import operator

from Api.DB import get_basket

from Widgets.Basket import product_info, pay

from config import KEYBOARD


async def getter_basket(dialog_manager: DialogManager, **kwargs):
    """Getter all cities from db."""
    user_id = dialog_manager.event.from_user.id
    products = await get_basket(user_id)
    return {
        "products": products,
        "count": len(products)
    }


async def choice_product_handler(
        callback: CallbackQuery,
        widget,
        manager: DialogManager,
        item_id: str
):
    """Handle to choose product from basket."""
    manager.dialog_data["basket_id"] = item_id
    await manager.switch_to(state=Basket.product_info)


async def switch(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(state=Basket.pay, show_mode=ShowMode.DELETE_AND_SEND)


window = Window(
    Const("Ваша корзина:"),
    Column(
        Select(
            Format("{item[0]}"),
            id="product_select",
            item_id_getter=operator.itemgetter(1),
            items="products",
            on_click=choice_product_handler,
        ),
    ),
    Button(Const("Оплатить"), id="pay", on_click=switch),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    markup_factory=KEYBOARD,
    getter=getter_basket,
    state=Basket.main,
)


dialog = Dialog(window, product_info.window, pay.window)
