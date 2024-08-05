"""this middlware need for checking what user is admin."""
from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from config import ADMINS


class CheckAdminMiddleware(BaseMiddleware):
    """Middlware class."""

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        """Check user and if he admin handle event"""
        user_id = data["event_from_user"].id
        if str(user_id) in ADMINS:
            return await handler(event, data)
