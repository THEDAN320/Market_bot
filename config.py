"""module for configuration data."""

from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.markup.inline_keyboard import InlineKeyboardFactory


TOKEN = "1625535953:AAH-17KfjZw49Xen0_esauEl8u78Me6dPEc"
INLINE = 1

ADMINS = "1107886401, 1362697375"

OPERATOR = "1107886401"

PAYMENTS = """
сбер | 89538823059
тинькофф | 89538823059
eth | 0000000000
"""

INSTRUCTION = """
Текст с инструкцией
"""

HELLO = """
Текст с приветствием
"""

CONTACTS = """
Текст с контактами
"""

ADMINS = ADMINS.replace(" ", "").split(",")
INSTRUCTION = INSTRUCTION[1:-1]
HELLO = HELLO[1:-1]
CONTACTS = CONTACTS[1:-1]
PAYMENTS = PAYMENTS[1:-1].split("\n")
PAYMENTS = [p.split("|", 1) for p in PAYMENTS]

if INLINE:
    KEYBOARD = InlineKeyboardFactory()
else:
    KEYBOARD = ReplyKeyboardFactory(resize_keyboard=True)
