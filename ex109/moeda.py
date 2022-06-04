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
