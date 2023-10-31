from inventory_report.product import Product


def test_create_product() -> None:
    config = {
        "id": "1",
        "product_name": "boardgame",
        "company_name": "hasbro",
        "manufacturing_date": "2021-08-01",
        "expiration_date": "2022-08-01",
        "serial_number": "123456",
        "storage_instructions": "keep in dry place",
    }
    instance = Product(**config)
    assert instance.id == "1"
    assert instance.product_name == "boardgame"
    assert instance.company_name == "hasbro"
    assert instance.manufacturing_date == "2021-08-01"
    assert instance.expiration_date == "2022-08-01"
    assert instance.serial_number == "123456"
    assert instance.storage_instructions == "keep in dry place"


def test_magic_method_str_from_product(capsys):
    config = {
        "id": "1",
        "product_name": "boardgame",
        "company_name": "hasbro",
        "manufacturing_date": "2021-08-01",
        "expiration_date": "2022-08-01",
        "serial_number": "123456",
        "storage_instructions": "keep in dry place",
    }
    instance = Product(**config)

    expected_output = (
        "The product 1 - boardgame with serial number 123456 "
        "manufactured on 2021-08-01 by the company hasbro valid"
        " until 2022-08-01 must be stored according to the following "
        "instructions: keep in dry place.\n"
    )
    print(instance.__str__()) # print(str(instance))
    captured = capsys.readouterr()
    assert captured.out == expected_output
