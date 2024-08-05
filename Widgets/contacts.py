"""instruction window."""
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from States.states import Menu

from config import CONTACTS, KEYBOARD


window = Window(
    Const(CONTACTS),
    SwitchTo(Const("‹ Назад"), id="contacts", state=Menu.main),
    markup_factory=KEYBOARD,
    state=Menu.contacts,
)
