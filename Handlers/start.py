"""code for handle /start command."""
from Api.DB import register_user

from States.states import Menu

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode, ShowMode


router = Router()


@router.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager) -> None:
    """Handle /start handler."""
    await register_user(message.from_user.id)
    await dialog_manager.start(state=Menu.main, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND)
