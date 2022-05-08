lista_de_pessoas = []
lista_de_mulheres = []
pessoa = {}
média_de_idade = 0

while True:
    pessoa['nome'] = str(input("Nome: ")).strip().capitalize()
    pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]

    while pessoa['sexo'] not in "MF":
        print("ERRO! Responda apenas M ou F")
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if pessoa['sexo'] == "F":
        lista_de_mulheres.append(pessoa['nome'])

    pessoa['idade'] = int(input("Idade: "))
    lista_de_pessoas.append(pessoa.copy())

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    while continuar not in "SN":
        print("ERRO! Responda apenas S ou N")
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if continuar == "N":
        break

for c in range(0, len(lista_de_pessoas)):
    média_de_idade += lista_de_pessoas[c]['idade']

média_de_idade = média_de_idade / len(lista_de_pessoas)
print(lista_de_mulheres)

print("-=" * 50)
print(f"A) Ao todo temos {len(lista_de_pessoas)} pessoas cadastradas.")
print(f"B) A média de idade é de {média_de_idade:.2f} anos.")
print(f"C) As mulheres cadastradas foram:", end=" ")

for c in range(0, len(lista_de_mulheres)):
    print(f"{lista_de_mulheres[c]}", end=" ")

print("")
print(f"D) Lista de pessoas que estão acima da média:")

for c in range(0, len(lista_de_pessoas)):
    if lista_de_pessoas[c]["idade"] > média_de_idade:
        print(f"    nome = {lista_de_pessoas[c]['nome']};", end=" ")
        print(f"sexo = {lista_de_pessoas[c]['sexo']};", end=" ")
        print(f"idade = {lista_de_pessoas[c]['idade']};", end=" ")
        print("")

print("<< ENCERRADO >>")
