from typing import List
from inventory_report.reports.complete_report import (
    SimpleReport,
    CompleteReport,
)
from inventory_report.inventory import Inventory
from inventory_report.importers import JsonImporter, CsvImporter


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """

    inventories = []
    if report_type == "simple":
        report = SimpleReport()
    elif report_type == "complete":
        report = CompleteReport()
    else:
        raise ValueError("Report type is invalid.")

    for path in file_paths:
        if path.endswith("json"):
            products = JsonImporter(path)
        else:
            products = CsvImporter(path)

        inventory = Inventory(products.import_data())

        inventories.append(inventory)

    for inventory in inventories:
        report.add_inventory(inventory)
    return report.generate()
