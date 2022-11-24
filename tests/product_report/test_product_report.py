from inventory_report.inventory.product import Product


def test_relatorio_produto():
    resturn1 = "O produto arroz fabricado em 22-02-02 por BlackSuit com"
    resturn2 = " validade até 12-12-12 precisa ser armazenado numa panela com "
    resturn3 = "carvão dentro."
    new_product = Product(
        22,
        "arroz",
        "BlackSuit",
        "22-02-02",
        "12-12-12",
        "4f6s5d4fs21c5sdr8g4d",
        "numa panela com carvão dentro",
    )
    assert new_product.__repr__() == resturn1 + resturn2 + resturn3
