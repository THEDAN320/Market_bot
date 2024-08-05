"""File for connect all dialogs and handlers to main router."""
from aiogram import Router

from Widgets.GetProduct import all_geters
from Widgets.Catalog import catalog
from Widgets.Basket import basket
from Widgets import (
    main_menu, admin_menu
)

from Handlers import (
    start, admin
)


main_router = Router()

# connect handlers
main_router.include_router(start.router)
main_router.include_router(admin.router)

# connect dialogs
main_router.include_router(main_menu.dialog)
main_router.include_router(admin_menu.dialog)
main_router.include_router(all_geters.dialog)
main_router.include_router(catalog.dialog)
main_router.include_router(basket.dialog)
