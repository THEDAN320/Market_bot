"""getter for city name."""
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Button, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Catalog, Basket

from Api.DB import (
    get_product, add_to_basket, product_in_basket,
    delete_basket_product_by_product
)

from config import KEYBOARD


async def getter_product(dialog_manager: DialogManager, **kwargs):
    """Getter product data from db by id."""
    product_id = dialog_manager.dialog_data["product_id"]
    product = await get_product(product_id)
    user_id = dialog_manager.event.from_user.id
    in_basket = await product_in_basket(user_id, product_id)
    dialog_manager.dialog_data["in_basket"] = in_basket
    if in_basket:
        action = "Убрать из корзины"
    else:
        action = "Добавить в корзину"
    return {
        "product_name": product[0],
        "product_description": product[1],
        "product_price": product[2],
        "action": action,
    }


async def add_product_to_basket(callback: CallbackQuery, button: Button, manager: DialogManager):
    """Handle to add product to basket."""
    user_id = manager.event.from_user.id
    product_id = manager.dialog_data["product_id"]
    in_basket = manager.dialog_data["in_basket"]
    if in_basket:
        await delete_basket_product_by_product(user_id, product_id)
        await manager.event.bot.send_message(user_id, "Товар убран!")
        await manager.switch_to(state=Catalog.product_info)
    else:
        await add_to_basket(user_id, product_id)
        await manager.event.bot.send_message(user_id, "Товар добавлен в корзину!")
        await manager.switch_to(state=Catalog.product_info)


window = Window(
    Format("Товар: {product_name}\n"),
    Format("Описание:\n{product_description}\n"),
    Format("Цена: {product_price}"),
    Button(Format("{action}"), id="add_to_basket", on_click=add_product_to_basket),
    SwitchTo(Const("‹ Назад"), id="back_to_choice_product", state=Catalog.choice_product),
    Start(Const("🛒 Перейти к корзине"), id="to_basket", state=Basket.main),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    markup_factory=KEYBOARD,
    getter=getter_product,
    state=Catalog.product_info,
)
