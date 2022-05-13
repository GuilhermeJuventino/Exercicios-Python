def ficha(nome=None, gols=None):
    """
    -> Gera uma ficha de jogador de futebol baseada nos 2 parametros opcionais.
    :param nome: (Opcional) Nome do jogador.
    :param gols: (Opcional) Número de gols do jogador.
    :return: Retorna o nome do jogador (Se não informado: o parametro retorna 'desconhecido')
    e o número de gols feitos no campeonato (Se não informado ou digitado incorretamente: o parametro retorna 0)
    """
    if not gols:
        gols = int(0)

    elif str(gols) not in "1234567890":
        gols = int(0)

    if not nome:
        nome = "<desconhecido>"

    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


# Programa principal.
print("-" * 52)

nome = str(input("Nome do jogador: ")).strip().capitalize()
número_de_gols = str(input("Número de gols: "))

print(ficha(nome, número_de_gols))
