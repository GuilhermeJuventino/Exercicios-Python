def leiaInt(frase):
    print("-" * 32)

    while True:
        texto = str(input(frase))

        if texto.isnumeric():
            texto = int(texto)
            return texto

        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")


# Programa principal
n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
