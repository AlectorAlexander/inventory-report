from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        lista_arquivos = []
        with open(path, encoding="utf-8") as file:
            response = csv.DictReader(file, delimiter=",", quotechar='"')
            for arq in response:
                lista_arquivos.append(arq)
        return lista_arquivos
