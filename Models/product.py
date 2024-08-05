"""dataclass model for product."""
from dataclasses import dataclass


@dataclass
class Product:
    """Class for keeping info about product."""

    title: str = "Без названия"
    description: str = ""
    price: str = "Не указана"
