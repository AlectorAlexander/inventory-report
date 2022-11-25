from inventory_report.importer.importer import Importer
import xmltodict
import json


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path) as fd:
                xml = xmltodict.parse(fd.read())
                jSON = json.dumps(xml)
                response = json.loads(jSON)
                lista_arquivos = response["dataset"]["record"]
            return lista_arquivos
        else:
            raise ValueError("Arquivo inválido")
