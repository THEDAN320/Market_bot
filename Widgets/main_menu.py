"""main menu dialog."""
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Row, Start, SwitchTo
from aiogram_dialog.widgets.text import Const
from States.states import Menu, Basket, Catalog

from Widgets import instruction, contacts

from config import HELLO, KEYBOARD


main_window = Window(
    Const(HELLO),
    Row(
        Start(Const("🛍️ За покупками"), id="to_catalog", state=Catalog.choice_city),
        Start(Const("🛒 Перейти к корзине"), id="to_basket", state=Basket.main),
    ),
    Row(
        SwitchTo(Const("📕 Инструкция"), id="instruction", state=Menu.instruction),
        SwitchTo(Const("👤 Контакты"), id="contacts", state=Menu.contacts),
    ),
    markup_factory=KEYBOARD,
    state=Menu.main,
)


dialog = Dialog(main_window, instruction.window, contacts.window)
