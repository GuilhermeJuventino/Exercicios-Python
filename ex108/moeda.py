def metade(preço=0):
    resultado = preço / 2
    return resultado


def dobro(preço=0):
    resultado = preço * 2
    return resultado


def aumentar(preço=0, taxa=0):
    resultado = preço + (preço * taxa / 100)
    return resultado


def diminuir(preço=0, taxa=0):
    resultado = preço - (preço * taxa / 100)
    return resultado


def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:.2f}".replace(".", ",")
