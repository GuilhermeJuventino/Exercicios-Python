from time import sleep

cores = {
    'branco': '\033[0;40;7m',
    'vermelho': '\033[0;41m',
    'verde': '\033[0;42m',
    'azul': '\033[0;44m',
    'normal': '\033[m'
}


def ajuda():
    while True:
        # Titulo
        print(f"{cores['verde']}", end="")
        print("~" * 30)
        print("Sistema de ajuda PyHelp")
        print("~" * 30)
        sleep(1)

        print(f"{cores['normal']}")
        alvo = str(input("Função ou biblioteca (Digite 'Fim' para sair) > ")).strip()

        # Checar se o usuário quer sair
        if alvo.lower() == "fim":
            # Fechando a função
            print(f"{cores['vermelho']}", end="")

            print("~" * 20)
            print("Até logo!")
            print("~" * 20)

            break

        # Acessando o manual da função/biblioteca expecificada
        print(f"{cores['azul']}", end="")

        print("~" * 38)
        print(f"Acessando o manual do comando '{alvo}'")
        print("~" * 38)

        print(f"{cores['normal']}")
        sleep(2)

        # Mostrando o manual na tela
        print(f"{cores['branco']}", end="")
        print(help(alvo))

        print(f"{cores['normal']}")


# Programa principal
ajuda()
