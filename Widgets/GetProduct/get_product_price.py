"""getter for product price."""
from aiogram.types import Message

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import SwitchTo, Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput

from States.admin import Admin, AddProduct

from Api.Save import save_product


async def handle_input(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        value: str
) -> None:
    """Handle user input for current input detail."""
    dialog_manager.dialog_data["product_price"] = value
    await save_product(dialog_manager)
    await message.answer("✅ Товар добавлен!")
    await dialog_manager.start(state=Admin.main)


window = Window(
    Const("Введите цену товара:"),
    SwitchTo(Const("‹ Назад"), id="back_to_get_product_description", state=AddProduct.get_product_description),
    Start(Const("В меню"), id="back_to_admin_menu", state=Admin.main),
    TextInput(id="get_product_price_input", on_success=handle_input),
    state=AddProduct.get_product_price,
)
