from inventory_report.product import Product
from typing import Optional


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        self.__data: list[Product] = [] if not data else data

    def add_data(self, data: list[Product]) -> None:
        for product in data:
            self.__data.append(product)

    @property
    def data(self) -> list[Product]:
        return self.__data
