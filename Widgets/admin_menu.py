"""admin menu dialog."""
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from States.admin import Admin, AddProduct


admin_window = Window(
    Const("Админ панель бота."),
    Start(Const("Добавить товар вручную"), id="input_add_file", state=AddProduct.get_city),
    Start(Const("Добавить .xlsx файлом"), id="file_add_product", state=AddProduct.get_file),
    state=Admin.main,
)


dialog = Dialog(admin_window)
