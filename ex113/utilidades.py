import sys


def leiaInt(frase):
    print("-" * 32)

    while True:
        try:
            texto = str(input(frase))

            texto = int(texto)

        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")

        except KeyboardInterrupt:
            print()
            print("\033[31mERRO! Você não digitou nenhum número.\033[m")
            sys.exit()

        else:
            return texto


def leiaFloat(frase):
    print("-" * 32)

    while True:
        try:
            texto = str(input(frase))

            texto = float(texto)

        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número flutuante válido.\033[m")

        except KeyboardInterrupt:
            print()
            print("\033[31mERRO! Você não digitou nenhum número.\033[m")
            sys.exit()

        else:
            return texto
