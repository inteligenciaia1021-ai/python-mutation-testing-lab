import pytest
from desconto import aplicar_desconto

def test_desconto_de_10_porcento():
    assert aplicar_desconto(100, 10) == 90

def test_desconto_de_50_porcento():
    assert aplicar_desconto(200, 50) == 100

def test_desconto_zero():
    assert aplicar_desconto(100, 0) == 100

def test_desconto_total():
    assert aplicar_desconto(100, 100) == 0

def test_desconto_negativo():
    with pytest.raises(ValueError, match="^Percentual inválido\\.$"):
        aplicar_desconto(100, -10)

def test_desconto_acima_de_100():
    with pytest.raises(ValueError, match="^Percentual inválido\\.$"):
        aplicar_desconto(100, 110)