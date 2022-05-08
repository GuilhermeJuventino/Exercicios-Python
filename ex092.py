import datetime

trabalhador = {}

nome = str(input("nome: ")).strip().capitalize()
ano_de_nascimento = int(input("Ano de nascimento: "))
cpts = int(input("CPTS (0 não tem): "))

ano_atual = datetime.datetime.now().year

trabalhador["nome"] = nome
trabalhador["idade"] = ano_atual - ano_de_nascimento
trabalhador["CPTS"] = cpts

if cpts != 0:
    ano_de_contratação = int(input("Ano de contratação: "))
    salário = int(input("Salário: R$"))

    trabalhador["Ano de contratação:"] = ano_de_contratação
    trabalhador["salário"] = str(f"R${salário}")

    trabalhador["ano de aposentadoria"] = (ano_de_contratação - ano_de_nascimento) + 35

print("-=" * 40)

for k, v in trabalhador.items():
    print(f"{k}: {v}")
