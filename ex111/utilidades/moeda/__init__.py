def metade(preço=0, formatar=False):
    """

    :param preço: O preço/valor a ser calculado.
    :param formatar: Opcional: Se verdadeiro(True) converte o resultado em valor monetário.
    :return: Retorna a metade do valor no parametro preço.
    """
    resultado = preço / 2

    if formatar:
        return moeda(resultado)

    return resultado


def dobro(preço=0, formatar=False):
    """

    :param preço: O preço/valor a ser calculado.
    :param formatar: Se verdadeiro(True) converte o resultado em valor monetário.
    :return: Retorna o dobro do valor no parametro preço.
    """
    resultado = preço * 2

    if formatar:
        return moeda(resultado)

    return resultado


def aumentar(preço=0, taxa=0, formatar=False):
    """

    :param preço: O preço/valor a ser calculado.
    :param taxa: (Opcional, padrão 0%) A taxa ou porcentagem pelo qual o valor sera aumentado.
    :param formatar: Se verdadeiro(True) converte o resultado em valor monetário.
    :return: Retorna o valor do parametro preço aumentado pela porcentagem do parametro taxa.
    """
    resultado = preço + (preço * taxa / 100)

    if formatar:
        return moeda(resultado)

    return resultado


def diminuir(preço=0, taxa=0, formatar=False):
    """

    :param preço: O preço/valor a ser calculado.
    :param taxa: (Opcional, padrão 0%) A taxa ou porcentagem pelo qual o valor sera diminuido.
    :param formatar: Se verdadeiro(True) converte o resultado em valor monetário.
    :return: Retorna o valor do parametro preço diminuido pela porcentagem do parametro taxa.
    """
    resultado = preço - (preço * taxa / 100)

    if formatar:
        return moeda(resultado)

    return resultado


def moeda(preço=0, moeda="R$"):
    """

    :param preço: (Opcional, padrão 0) Valor a ser formatado.
    :param moeda: (Opcional, padrão R$) A moeda pra o qual o valor de preço sera formatada. (R$, U$, etc.)
    :return: Retorna uma string com o valor do parametro preço em formatação monetária.
    """
    return f"{moeda}{preço:.2f}".replace(".", ",")


def resumo(preço=0, aumento=10, redução=10):
    """
    Cria um resumo com várias informações sobre o valor informado no parâmetro preço
    utilizando as outras funções do módulo moeda.
    :param preço:(Opcional: Padrão 0) Preço a ser calculado.
    :param aumento:(Opcional: Padrão 10) Taxa de aumento do preço.
    :param redução:(Opcional: Padrão 10) Taxa de redução do preço.
    :return: (Sem retorno)
    """
    print("-" * 32)
    print(f"RESUMO DO VALOR".center(30))
    print("-" * 32)

    print(f"Preço analizado: \t{moeda(preço)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(preço, aumento, True)}")
    print(f"{redução}% de redução: \t{diminuir(preço, redução, True)}")

    print("-" * 32)
