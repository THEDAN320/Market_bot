"""code for handle /admin command."""
from Api.DB import register_user

from States.admin import Admin

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from Middlwares.check_admin import CheckAdminMiddleware


router = Router()
router.message.middleware(CheckAdminMiddleware())


@router.message(Command("admin"))
async def admin(message: Message, dialog_manager: DialogManager) -> None:
    """Handle /admin handler."""
    print(message.text)
    await register_user(message.from_user.id)
    await dialog_manager.start(state=Admin.main, mode=StartMode.RESET_STACK)
