lista_de_valores = []

for c in range(0, 5):
    valor = int(input("Digite um valor: "))

    # Se o contador for igual a 0 ou o valor inserido for maior que o maior número na lista,
    # O valor sera inserido no final da lista.
    if c == 0 or valor > lista_de_valores[-1]:
        lista_de_valores.append(valor)
        print("Valor inserido no FINAL da lista.")

    # Se não, um contador chamado "pos" sera criado começando com 0.
    else:
        pos = 0

        # Enquanto o contador for igual a 0,
        # O programa irá checar se o valor inserido é menor ou igual ao valor na posição do contador.
        while pos < len(lista_de_valores):

            # Se o valor inserido for menor ou igual ao valor na posição do contador,
            # O valor digitado sera inserido na posição atual do contador. (Ou seja, antes do valor anterior.)
            if valor <= lista_de_valores[pos]:
                lista_de_valores.insert(pos, valor)

                # Avisa ao usuário que o valor foi inserido no começo da lista se o contador for igual a 0.
                if pos == 0:
                    print("Valor inserido no COMEÇO da lista.")

                # Se o contador não for mais igual a 0 e o novo valor não for inserido no final da lista,
                # O programa irá mostrar em que posição o novo valor foi inserido.
                else:
                    print(f"Valor inserido na posição {pos}.")

                break

            # Após o final da repetição while, o programa irá adicionar 1 ao contador.
            pos += 1

# E no final o programa irá mostrar a lista dos 5 valores digitados em ordem crescente.
print(f"Valores digitados em ordem: {lista_de_valores}")
