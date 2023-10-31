from dataclasses import dataclass
from inventory_report.product import Product


@dataclass
class Inventory:
    __data: list[Product] = list()

    def add_data(self, data: Product) -> None:
        self.__data.append(data)

    @property
    def data(self) -> list[Product]:
        return self.__data
