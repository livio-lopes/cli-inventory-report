from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory

from datetime import date


class SimpleReport(Report):
    def __init__(self) -> None:
        self._reports: list[Inventory] = list()

    def add_inventory(self, inventory: Inventory) -> None:
        self._reports.append(inventory)

    def oldest_produced(self) -> str:
        oldest = date.today()
        for inventory in self._reports:
            for product in inventory.data:
                date_product = date.fromisoformat(product.manufacturing_date)
                if date_product < oldest:
                    oldest = date_product
        return str(oldest)

    def to_expire(self) -> str:
        today = date.today()
        dates: dict[str, int] = {}
        for inventory in self._reports:
            for product in inventory.data:
                difference = (
                    date.fromisoformat(product.expiration_date) - today
                )
                dates[product.expiration_date] = difference.days

        filtered = sorted([key for key, value in dates.items() if value > 0])[
            0
        ]
        return filtered

    def largest_company(self) -> str:
        companies: dict[str, int] = {}

        for inventory in self._reports:
            for product in inventory.data:
                if product.company_name not in companies:
                    companies[product.company_name] = 1
                else:
                    companies[product.company_name] += 1

        return max(companies.keys())

    def generate(self) -> str:
        output = (
            f"Oldest manufacturing date: {self.oldest_produced()}\n"
            f"Closest expiration date: {self.to_expire()}\n"
            f"Company with the largest inventory: {self.largest_company()}\n"
        )

        return output
