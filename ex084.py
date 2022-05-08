lista_de_pessoas = []
pessoas = []
pessoas_mais_leves = []
pessoas_mais_pesadas = []
maior = menor = 0

while True:
    # Guardando o nome de várias pessoas em uma lista
    pessoa = str(input("Nome: ")).strip().capitalize()
    peso = float(input("Peso: "))

    pessoas.append(pessoa)
    pessoas.append(peso)

    if len(lista_de_pessoas) == 0:
        maior = menor = pessoas[1]

    else:
        if pessoas[1] > maior:
            maior = pessoas[1]

        elif pessoas[1] < menor:
            menor = pessoas[1]

    lista_de_pessoas.append(pessoas[:])
    pessoas.clear()

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if continuar == "N":
        break

# Determinando quantas pessoas foram cadastradas
print("-=" * 30)
print(f"{len(lista_de_pessoas)} foram cadastradas.")
print("-=" * 30)

# Determinando quais são as pessoas mais pesadas e mais leves
print(f"As pessoas mais leves são...")
for p in lista_de_pessoas:
    if p[1] == menor:
        print(f"{p[0]} ", end="")

print("\nAs pessoas mais pesadas são...")
for p in lista_de_pessoas:
    if p[1] == maior:
        print(f"{p[0]} ", end="")
