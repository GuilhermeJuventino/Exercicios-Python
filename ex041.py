from datetime import date

ano_atual = date.today().year
data_de_nascimento = int(input("Qual é o seu ano de nascimento? "))
idade = ano_atual - data_de_nascimento

print("""Os atletas serão classificados de acordo com sua idade.

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER""")

print("Você tem {} anos.".format(idade))

if idade <= 9:
    print("Você será classificado como atleta MIRIM.")
elif idade <= 14:
    print("Você será classificado como atleta INFANTIL.")
elif idade <= 19:
    print("Você será classificado como atleta JÚNIOR.")
elif idade <= 25:
    print("Você será classificado como atleta SÊNIOR.")
else:
    print("Você será classificado como atleta MASTER.")
