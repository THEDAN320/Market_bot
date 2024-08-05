"""getter for xlsx file."""
from aiogram.types import Message, Document

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import MessageInput

from States.admin import Admin, AddProduct
from Api.Save import save_with_xlsx
from config import TOKEN

from io import BytesIO

import aiohttp


async def get_photo_bytes(file: Document) -> bytes:
    """By ашду object with telegram api get file bytes."""
    file_data = await file.bot.get_file(file.file_id)
    file_path = file_data.file_path
    file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'

    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            return await response.read()


async def handle_input(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager
):
    """Handle user input for current input detail."""
    document = message.document
    if document and document.file_name.endswith(".xlsx"):
        file_bytes = await get_photo_bytes(document)
        await save_with_xlsx(BytesIO(file_bytes))
        await message.answer("✅ Товары успешно добавлены!")
        await dialog_manager.start(state=Admin.main)
    else:
        await message.answer("Неверный формат файла!")


window = Window(
    Const("Отправьте свой xlsx файл:"),
    Start(Const("В меню"), id="back_to_admin_menu", state=Admin.main),
    MessageInput(handle_input),
    state=AddProduct.get_file,
)
