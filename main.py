"""main file."""
import asyncio
import logging
import logging.config
import signal
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import setup_dialogs

from config import TOKEN

logging.config.fileConfig("logging.ini")


def signal_handler(sig, frame):
    """обработчик остановки бота для удобства."""
    logging.info("Bot has stoped!")
    sys.exit(0)


async def main():
    """запуск поллинга для бота."""
    signal.signal(signal.SIGINT, signal_handler)
    logging.basicConfig(level=logging.INFO)

    # получаем токен и создаем объект бота
    bot = Bot(token=TOKEN[:46])
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    setup_dialogs(dp)

    # удаляем вебхуки и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
