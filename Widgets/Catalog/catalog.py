"""join all geters to one dialog."""
from aiogram_dialog import Dialog

from Widgets.Catalog import (
    choice_city, choice_address, choice_product, product_info
)


dialog = Dialog(
    choice_city.window, choice_address.window,
    choice_product.window, product_info.window
)
