"""api for usage database."""
import aiosqlite

from sqlite3 import Row

from typing import Optional, Iterable

from Models.product import Product

DB_NAME = "database.db"


async def register_user(user_id: int | str) -> None:
    """Register user in db."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO USERS(telegram_id) VALUES(?);", (user_id,))
        await db.commit()


async def add_city(city_name: str) -> Optional[int]:
    """Add new city to db."""
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("INSERT INTO CITIES(name) VALUES(?);", (city_name,))
        await db.commit()
        return cursor.lastrowid


async def get_city(city_name: str) -> Optional[int]:
    """Get city id by their name from db."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM CITIES WHERE name = ?", (city_name,)) as cursor:
            data = await cursor.fetchone()
            return data if data is None else data[0]


async def get_cities() -> Iterable[Row]:
    """Get data all cities in db."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT name, id FROM CITIES") as cursor:
            data = await cursor.fetchall()
            return data


async def add_address(address: str, city_id: int) -> Optional[int]:
    """Add new city to db."""
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("INSERT INTO ADDRESS(name, city_id) VALUES(?, ?);", (address, city_id))
        await db.commit()
        return cursor.lastrowid


async def get_addres(addres_name: str, city_id: int) -> Optional[int]:
    """Get address id by their name from db."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT * FROM ADDRESS WHERE name = ? AND city_id = ?",
            (addres_name, city_id)
        ) as cursor:
            data = await cursor.fetchone()
            return data if data is None else data[0]


async def get_addreses(city_id: int) -> Iterable[Row]:
    """Get data all addreses by city id in db."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT name, id FROM ADDRESS WHERE city_id = ?", (int(city_id),)) as cursor:
            data = await cursor.fetchall()
            return data


async def add_product(product: Product, address_id: int) -> None:
    """Add new product to db."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO PRODUCTS(title, description, price, address_id) VALUES(?, ?, ?, ?);",
            (product.title, product.description, product.price, address_id)
        )
        await db.commit()


async def get_products(address_id: int) -> Iterable[Row]:
    """Get data all products by address id in db."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT title, id FROM PRODUCTS WHERE address_id = ?", (int(address_id),)) as cursor:
            data = await cursor.fetchall()
            return data


async def get_product(product_id: int) -> Optional[Iterable[Row]]:
    """Get data about product by id from db."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT title, description, price FROM PRODUCTS WHERE id = ?",
            (int(product_id),)
        ) as cursor:
            data = await cursor.fetchone()
            return data


async def product_in_basket(user_id: int | str, product_id: int) -> bool:
    """Return True if product in user basket else False."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT id FROM CATALOG WHERE user_id = ? AND product_id = ?",
            (user_id, int(product_id),)
        ) as cursor:
            data = await cursor.fetchone()
            return data != None


async def add_to_basket(user_id: int | str, product_id: int) -> None:
    """Add product to user basket."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO CATALOG(user_id, product_id) VALUES(?, ?);",
            (user_id, int(product_id))
        )
        await db.commit()


async def get_basket(user_id: int | str) -> Iterable[Row]:
    """Get user basket by id."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            (
                "SELECT PRODUCTS.title, CATALOG.id as catalog_id "
                "FROM CATALOG JOIN PRODUCTS ON CATALOG.product_id = PRODUCTS.id WHERE user_id = ?"
            ),
            (user_id,)
        ) as cursor:
            data = await cursor.fetchall()
            return data


async def get_all_basket_info(user_id: int | str) -> Iterable[Row]:
    """Get user basket by id."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            (
                "SELECT PRODUCTS.title, PRODUCTS.description, PRODUCTS.price, CATALOG.id as catalog_id "
                "FROM CATALOG JOIN PRODUCTS ON CATALOG.product_id = PRODUCTS.id WHERE user_id = ?"
            ),
            (user_id,)
        ) as cursor:
            data = await cursor.fetchall()
            return data


async def get_basket_product(basket_id: int) -> Optional[Iterable[Row]]:
    """Get basket product with id."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT product_id FROM CATALOG WHERE id = ?",
            (basket_id,)
        ) as cursor:
            data = await cursor.fetchone()
            return data if data is None else data[0]


async def delete_basket_product(basket_id: int) -> None:
    """Delete product from id."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM CATALOG WHERE id = ?",
            (int(basket_id),)
        )
        await db.commit()


async def delete_basket_product_by_product(user_id: str | int, product_id: int) -> None:
    """Delete product from id."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM CATALOG WHERE user_id = ? AND product_id = ?",
            (user_id, int(product_id),)
        )
        await db.commit()
