from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str):
        super().__init__(path)

    def import_data(self) -> list[Product]:
        with open(self.path) as json_file:
            data = json.load(json_file)
            products = []
            for product in data:
                products.append(Product(**product))
            return products


class CsvImporter(Importer):
    def __init__(self, path: str) -> None:
        self.path = path

    def import_data(self) -> list[Product]:
        list_product = list()
        with open(self.path) as csv_file:
            data = csv.DictReader(csv_file)
            for product in data:
                list_product.append(Product(**product))
        return list_product


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
