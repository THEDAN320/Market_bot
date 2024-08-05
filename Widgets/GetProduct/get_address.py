"""getter for address."""
from aiogram.types import Message

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import SwitchTo, Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput

from States.admin import Admin, AddProduct


async def handle_input(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        value: str
) -> None:
    """Handle user input for current input detail."""
    dialog_manager.dialog_data["address"] = value
    await dialog_manager.switch_to(state=AddProduct.get_product_name)


window = Window(
    Const("Введите улицу/метро/адрес:"),
    SwitchTo(Const("‹ Назад"), id="back_to_get_city", state=AddProduct.get_city),
    Start(Const("В меню"), id="back_to_admin_menu", state=Admin.main),
    TextInput(id="get_address_input", on_success=handle_input),
    state=AddProduct.get_address,
)
