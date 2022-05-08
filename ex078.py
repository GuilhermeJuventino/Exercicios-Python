lista_de_valores = []
posições_maior = []
posições_menor = []

# Guarda todos os números inteiros digitados dentro de uma lista.
for posição in range(0, 5):
    lista_de_valores.append(int(input(f"Digite um valor para a posição {posição}: ")))

# Guarda as posições do maior e menor valor da lista. (incluindo valores repetidos.)
for posição, valores in enumerate(lista_de_valores):
    if valores == max(lista_de_valores):
        posições_maior.append(posição)

    if valores == min(lista_de_valores):
        posições_menor.append(posição)

# Mostra todos os valores digitados na tela.
print(f"Você digitou os valores {lista_de_valores}")
# Mostra qual foi o maior e menor valor digitado, e em quais posições eles aparecem.
print(f"O maior valor na lista é {max(lista_de_valores)} nas posições ", end="")

for posição, valores in enumerate(posições_maior):
    print(f"{valores}... ", end="")

print(f"\nO menor valor na lista é {min(lista_de_valores)} nas posições ", end="")

for posição, valores in enumerate(posições_menor):
    print(f"{valores}... ", end="")
