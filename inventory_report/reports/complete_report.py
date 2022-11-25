from inventory_report.reports.simple_report import SimpleReport
import collections


class CompleteReport(SimpleReport):
    @classmethod
    def adicionalText(cls, empresas):
        frequencia = collections.Counter(empresas).most_common()
        unique_list = list()

        for i in range(len(frequencia)):
            if frequencia[i] not in frequencia[i + 1:]:
                unique_list.append(frequencia[i])

        text = ""
        for empresa in unique_list:
            text += f"- {empresa[0]}: {empresa[1]}\n"
        return text

    @classmethod
    def generate(cls, stock):
        response = cls.setItems(stock)

        data_de_validade = cls.validadeMaisRecente(
            response["datas_de_validade"]
        )

        nome_da_empresa = cls.empresaMaior(response["nomes_da_empresa"])

        text = cls.adicionalText(response["nomes_da_empresa"])

        data_de_fabricacao = cls.fabricacaoMaisAntiga(
            response["datas_de_fabricacao"]
        )
        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {nome_da_empresa}\n"
            f"Produtos estocados por empresa:\n"
            f"{text}"
        )


test = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 2,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2022-11-30",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 2,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Nature",
        "data_de_fabricacao": "2020-04-04",
        "data_de_validade": "2023-11-30",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]

print(CompleteReport().generate(test))
