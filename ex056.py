soma_idade = 0
média_idade = 0
mulheres20 = 0
N_homen_mais_velho = ""
I_homen_mais_velho = 0
pessoas = 1

while True:
    print(f"----- {pessoas}ª PESSOA -----")
    pessoas += 1
    nome = str(input("Nome: ")).capitalize().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    soma_idade += idade
    if sexo == "F" and idade < 20:
        mulheres20 += 1
    if sexo == "M" and idade > I_homen_mais_velho:
        I_homen_mais_velho = idade
        N_homen_mais_velho = nome
    if continuar == "N":
        break

média_idade = soma_idade / pessoas

print("A média de idade do grupo é de {:.0f} anos".format(média_idade))
print(f"O homen mais velho tem {I_homen_mais_velho} anos e se chama {N_homen_mais_velho}.")
print(f"Ao todo são {mulheres20} mulheres com menos de 20 anos")
