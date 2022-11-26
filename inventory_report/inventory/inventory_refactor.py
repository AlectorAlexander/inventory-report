from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, Importer):
        self.importer = Importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, forma):
        lista_arquivos = self.importer.import_data(path)
        self.data = [*self.data, *lista_arquivos]

        if forma == "simples":
            return SimpleReport().generate(lista_arquivos)
        if forma == "completo":
            return CompleteReport().generate(lista_arquivos)
