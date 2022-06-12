def leiaDinheiro(msg):
    """
    lê o input do usuário, troca todas as virgulas (,) na string para pontos (.),
    e se o valor final for válido (Ou seja, pode ser convertido para float) retorna o valor final convertido.

    :param msg: Mensagem de instrução para o usuário (Similar ao comando input())
    :return: Se válido retorna o valor digitado pelo usuário convertido para float. Do contrário retorna um erro.
    """

    while True:
        valor = str(input(msg)).replace(",", ".").strip()

        if valor.isalpha() or valor == "":
            print(f"\033[0;31mERRO: \"{valor}\" é um preço inválido!\033[m")

        else:
            return float(valor)
