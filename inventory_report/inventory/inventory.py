import csv
import xmltodict
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
    def xmlCase(cls, path):
        with open(path) as fd:
            xml = xmltodict.parse(fd.read())
            jSON = json.dumps(xml)
            response = json.loads(jSON)
            lista_arquivos = response["dataset"]["record"]
        return lista_arquivos

    def just_in_the_case(path):
        if path.endswith(".csv"):
            lista_arquivos = Inventory.csvCase(path)
        elif path.endswith(".json"):
            lista_arquivos = Inventory.jsonCase(path)
        elif path.endswith(".xml"):
            lista_arquivos = Inventory.xmlCase(path)
        return lista_arquivos

    @classmethod
    def import_data(cls, caminho, forma):
        lista_arquivos = Inventory.just_in_the_case(caminho)

        if forma == "simples":
            return SimpleReport().generate(lista_arquivos)
        if forma == "completo":
            return CompleteReport().generate(lista_arquivos)
