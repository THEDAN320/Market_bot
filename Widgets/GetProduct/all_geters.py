"""join all geters to one dialog."""
from aiogram_dialog import Dialog

from Widgets.GetProduct import (
    get_city, get_address, get_product_name,
    get_product_description, get_product_price,
    get_xlsx
)


dialog = Dialog(
    get_city.window, get_address.window, get_product_name.window,
    get_product_description.window, get_product_price.window,
    get_xlsx.window
)
