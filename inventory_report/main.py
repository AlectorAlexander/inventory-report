import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def step_zero():
    print("Verifique os argumentos", file=sys.stderr)
    return


def csv_situation():
    response = InventoryRefactor(CsvImporter).import_data(
        path=sys.argv[1], forma=sys.argv[2]
    )
    print(response, end='')
    return response


def json_situation():
    response = InventoryRefactor(JsonImporter).import_data(
        path=sys.argv[1], forma=sys.argv[2]
    )
    print(response, end='')
    return response


def xml_situation():
    response = InventoryRefactor(XmlImporter).import_data(
        path=sys.argv[1], forma=sys.argv[2]
    )
    print(response, end='')
    return response


def main():
    if len(sys.argv) != 3:
        step_zero()

    if sys.argv[1].endswith(".csv"):
        csv_situation()

    elif sys.argv[1].endswith(".json"):
        json_situation()

    elif sys.argv[1].endswith(".xml"):
        xml_situation()
