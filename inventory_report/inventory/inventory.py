import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def csvCase(cls, path):
        lista_arquivos = []
        with open(path, encoding="utf-8") as file:
            response = csv.DictReader(file, delimiter=",", quotechar='"')
            for arq in response:
                lista_arquivos.append(arq)
        return lista_arquivos

    @classmethod
    def jsonCase(cls, path):
        lista_arquivos = []
        with open(path) as file:
            response = json.load(file)
            for arq in response:
                lista_arquivos.append(arq)
        return lista_arquivos

    @classmethod
    def import_data(cls, caminho, forma):
        lista_arquivos = None
        if caminho.endswith(".csv"):
            lista_arquivos = Inventory.csvCase(caminho)
        elif caminho.endswith(".json"):
            lista_arquivos = Inventory.jsonCase(caminho)

        if forma == "simples":
            return SimpleReport().generate(lista_arquivos)
        if forma == "completo":
            return CompleteReport().generate(lista_arquivos)
