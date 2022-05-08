lista_de_números = [[], []]

# Guardando sete números em uma lista única
for c in range(0, 7):
    número = int(input(f"{c + 1}o número: "))

    if número % 2 == 0:
        lista_de_números[0].append(número)

    else:
        lista_de_números[1].append(número)

# Mostrando as listas de números pares e ímpares em ordem crescente
print(f"Lista de números pares em ordem crescente: {sorted(lista_de_números[0])}")
print(f"Lista de números ímpares em ordem crescente: {sorted(lista_de_números[1])}")
