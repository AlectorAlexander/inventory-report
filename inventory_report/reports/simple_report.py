from datetime import date
import statistics


class SimpleReport:
    def __init__(self):
        self.items = []
        self.nome_da_empresa = ""
        self.data_de_fabricacao = ""
        self.data_de_validade = ""

    @classmethod
    def setItems(cls, stock):

        hoje = date.today().isoformat()

        nomes_da_empresa = []
        datas_de_fabricacao = []
        datas_de_validade = []

        for item in stock:
            nomes_da_empresa.append(item["nome_da_empresa"])
            datas_de_fabricacao.append(item["data_de_fabricacao"])
            if item["data_de_validade"] > hoje:
                datas_de_validade.append(item["data_de_validade"])

        return {
            "nomes_da_empresa": nomes_da_empresa,
            "datas_de_fabricacao": datas_de_fabricacao,
            "datas_de_validade": datas_de_validade,
        }

    @classmethod
    def fabricacaoMaisAntiga(cls, datas_de_fabricacao):
        return min(datas_de_fabricacao)

    @classmethod
    def validadeMaisRecente(cls, datas_de_validade):
        return min(datas_de_validade)

    @classmethod
    def empresaMaior(cls, nomes_da_empresa):
        return statistics.mode(nomes_da_empresa)

    @classmethod
    def generate(cls, stock):
        response = cls.setItems(stock)

        data_de_validade = cls.validadeMaisRecente(
            response["datas_de_validade"]
            )

        nome_da_empresa = cls.empresaMaior(
            response["nomes_da_empresa"]
            )

        data_de_fabricacao = cls.fabricacaoMaisAntiga(
            response["datas_de_fabricacao"]
        )

        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {nome_da_empresa}"
        )
