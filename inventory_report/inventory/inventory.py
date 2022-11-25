from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    def just_in_the_case(path):
        if path.endswith(".csv"):
            lista_arquivos = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            lista_arquivos = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            lista_arquivos = XmlImporter.import_data(path)
        else:
            raise ValueError("Arquivo inválido")
        return lista_arquivos

    @classmethod
    def import_data(cls, caminho, forma):
        lista_arquivos = Inventory.just_in_the_case(caminho)

        if forma == "simples":
            return SimpleReport().generate(lista_arquivos)
        if forma == "completo":
            return CompleteReport().generate(lista_arquivos)
