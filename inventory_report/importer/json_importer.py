from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        lista_arquivos = []
        with open(path) as file:
            response = json.load(file)
            for arq in response:
                lista_arquivos.append(arq)
        return lista_arquivos
