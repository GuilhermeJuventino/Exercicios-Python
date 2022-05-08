homens = 0
mulheres = 0
maiores_de_idade = 0
mulheres_20 = 0
homen_mais_velho = ""
idade_homen = 0
mulher_mais_velha = ""
idade_mulher = 0

print("------Analisador De Pessoas------")

while True:
    nome = str(input("Nome: ")).strip().capitalize()
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    idade = int(input("Idade: "))

    # Conta quantas pessoas com mais de 18 anos foram cadastradas.
    if idade > 18:
        maiores_de_idade += 1

    # Conta quantos homens foram cadastrados.
    if sexo == "M":
        homens += 1
        # Determina qual é o homen mais velho
        if idade > idade_homen:
            idade_homen = idade
            homen_mais_velho = nome

    # Conta quantas mulheres foram cadastradas.
    elif sexo == "F":
        mulheres += 1
        # Determina qual é a mulher mais velha.
        if idade > idade_mulher:
            idade_mulher = idade
            mulher_mais_velha = nome
        # Conta quantas mulheres com menos de 20 anos foram cadastradas.
        if idade < 20:
            mulheres_20 += 1

    # Pergunta para o usuário se ele quer continuar.
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    # Se o usuário digitar "N" o loop é encerrado.
    if continuar == "N":
        break

print(f"Ao todo, foram {homens} homens cadastrados, e {mulheres} mulheres cadastradas.")
print(f"Entre essas pessoas, {maiores_de_idade} tem mais de 18 anos.")
print(f"Entre as mulheres, {mulheres_20} delas tem menos de 20 anos.")
print(f"O homen mais velho cadastrado é {homen_mais_velho} com {idade_homen} anos.")
print(f"A mulher mais velha cadastrada é {mulher_mais_velha} com {idade_mulher} anos.")
