"""getter for city name."""
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Button, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Basket

from Api.DB import get_product, get_basket_product, delete_basket_product

from config import KEYBOARD


async def getter_product(dialog_manager: DialogManager, **kwargs):
    """Getter product data from db by id."""
    basket_id = dialog_manager.dialog_data["basket_id"]
    product_id = await get_basket_product(basket_id)
    product = await get_product(product_id)
    return {
        "product_name": product[0],
        "product_description": product[1],
        "product_price": product[2],
    }


async def delete_product_from_basket(callback: CallbackQuery, button: Button, manager: DialogManager):
    """Handle to delete product from basket."""
    basket_id = manager.dialog_data["basket_id"]
    await delete_basket_product(basket_id)
    user_id = manager.event.from_user.id
    await manager.event.bot.send_message(user_id, "Товар убран из корзины!")
    await manager.switch_to(state=Basket.main)


window = Window(
    Format("Товар: {product_name}\n"),
    Format("Описание:\n{product_description}\n"),
    Format("Цена: {product_price}"),
    Button(Const("Убрать из корзины"), id="delete_from_basket", on_click=delete_product_from_basket),
    SwitchTo(Const("‹ Назад"), id="back_to_basket", state=Basket.main),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    markup_factory=KEYBOARD,
    getter=getter_product,
    state=Basket.product_info,
)
