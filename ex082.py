# Gerando a lista de valores.
valores = []
valores_pares = []
valores_ímpares = []

while True:
    número = int(input("Digite um valor: "))
    valores.append(número)

    continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]

    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]

    if continuar in "Nn":
        break

for valor in valores:
    # Gerando a lista de números pares.
    if valor % 2 == 0:
        valores_pares.append(valor)

    # Gerando a lista de valores ímpares
    elif valor % 2 != 0:
        valores_ímpares.append(valor)

print("-=" * 30)
print(f"Lista de valores digitados: {valores}")

if len(valores_pares) > 0:
    print(f"Lista de valores pares: {valores_pares}")

else:
    print("Nenhum valor par foi digitado.")

if len(valores_ímpares) > 0:
    print(f"Lista de valores ímpares: {valores_ímpares}")

else:
    print("Nenhum valor ímpar foi digitado.")
