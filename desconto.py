def aplicar_desconto(preco, percentual):
    if percentual > 100 or percentual < 0:
        raise ValueError("Percentual inválido.")

    return preco * (1 - percentual / 100)