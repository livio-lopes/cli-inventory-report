from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self) -> None:
        super().__init__()

    def generate(self) -> str:
        simple_report = super().generate()
        lines_companies = "Stocked products by company:\n"
        for company, stock in sorted(self._companies.items(), reverse=True):
            lines_companies += f"- {company}: {stock}\n"
        return simple_report + lines_companies


