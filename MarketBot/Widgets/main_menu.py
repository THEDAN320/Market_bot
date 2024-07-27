"""main menu dialog."""
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Row, Start, SwitchTo
from aiogram_dialog.widgets.text import Const
from States.states import Menu, Basket, Catalog


main_window = Window(
    Const("Приветственный текст для пользователя"),
    Row(
        Start(Const("🛍️ За покупками"), id="to_catalog", state=Catalog.main),
        Start(Const("🛒 Перейти к корзине"), id="to_basket", state=Basket.main),
    ),
    Row(
        SwitchTo(Const("💬 Отзывы"), id="comments", state=Menu.comments),
        SwitchTo(Const("👤 Контакты"), id="contacts", state=Menu.contacts),
    ),
    SwitchTo(Const("📕 Инструкция"), id="instruction", state=Menu.instruction),
    state=Menu.main,
)


dialog = Dialog(main_window)
