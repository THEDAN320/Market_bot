"""getter for city name."""
from aiogram_dialog import Window, DialogManager, Dialog
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Url
from aiogram_dialog.widgets.text import Const, Format

from States.states import Menu, Basket

from Api.DB import get_all_basket_info

from Widgets.Basket import product_info

from config import OPERATOR, PAYMENTS


async def getter_basket(dialog_manager: DialogManager, **kwargs):
    """Getter all cities from db."""
    user_id = dialog_manager.event.from_user.id
    products = await get_all_basket_info(user_id)
    products_info: list[str] = []
    for data in products:
        products_info.append(
            f"Товар: {data[0]}\n" \
            f"Описание: {data[1]}\n" \
            f"Цена: {data[2]}\n"
        )
    payments = "\n".join([f"{data[0]} - {data[1]}" for data in PAYMENTS])
    return {
        "products": "\n\n".join(products_info),
        "pay_methods": payments
    }


window = Window(
    Const("Ваша корзина:"),
    Format("{products}\n"),
    Const("Способы оплаты:"),
    Format("{pay_methods}\n"),
    Const("После оплаты отправьте чек менеджеру!"),
    Url(Const("Связь с менеджером"), url=Const(f"tg://openmessage?user_id={OPERATOR}"), id="back_to_basket"),
    SwitchTo(Const("Назад"), id="back_to_basket", state=Basket.pay),
    Start(Const("В меню"), id="back_to_main_menu", state=Menu.main),
    getter=getter_basket,
    state=Basket.pay,
)


dialog = Dialog(window, product_info.window)
