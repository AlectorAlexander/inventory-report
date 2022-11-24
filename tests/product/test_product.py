from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        22,
        "arroz",
        "BlackSuit",
        "22-02-02",
        "12-12-12",
        "4f6s5d4fs21c5sdr8g4d",
        "jogue numa panela com carvão dentro, pule amarelinha, conte até 10",
    )
    d = "jogue numa panela com carvão dentro, pule amarelinha, conte até 10"
    assert new_product.id == 22
    assert new_product.nome_do_produto == "arroz"
    assert new_product.nome_da_empresa == "BlackSuit"
    assert new_product.data_de_fabricacao == "22-02-02"
    assert new_product.data_de_validade == "12-12-12"
    assert new_product.numero_de_serie == "4f6s5d4fs21c5sdr8g4d"
    assert new_product.instrucoes_de_armazenamento == d
