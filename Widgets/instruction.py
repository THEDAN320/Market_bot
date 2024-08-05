"""instruction window."""
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from States.states import Menu

from config import INSTRUCTION, KEYBOARD


window = Window(
    Const(INSTRUCTION),
    SwitchTo(Const("‹ Назад"), id="instruction", state=Menu.main),
    markup_factory=KEYBOARD,
    state=Menu.instruction,
)
