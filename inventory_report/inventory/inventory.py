import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, caminho, forma):
        lista_arquivos = []
        if caminho.endswith('.csv'):
            with open(caminho, encoding='utf-8') as file:
                response = csv.DictReader(file, delimiter=",", quotechar='"')
                for arq in response:
                    lista_arquivos.append(arq)
        if forma == "simples":
            return SimpleReport().generate(lista_arquivos)
        if forma == "completo":
            return CompleteReport().generate(lista_arquivos)
