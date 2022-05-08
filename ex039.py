from datetime import date

ano = int(input("Qual é a seu ano de nascimento? "))
ano_atual = date.today().year
idade = ano_atual - ano
sexo = str(input("Qual é o seu sexo? ")).lower().strip()

if sexo == "masculino":
    print("Pessoas do sexo masculino precisam fazer o alistamento militar obrigatório.")
    print("Quem nasceu em {} tem {} ano(s) em {}.".format(ano, idade, ano_atual))
    if idade == 18:
        print("CORRA! Esta na hora de se alistar ao serviço militar!")
    elif idade < 18:
        print("Ainda falta(m) {} ano(s) para você se alistar.".format(18 - idade))
        print("Seu alistamento será em {}.".format((18 - idade) + ano_atual))
    else:
        print("\033[31mVocê ja deveria ter se alistado há {} ano(s)\033[m".format(idade - 18))
        print("Seu alistamento foi em {}".format((ano_atual + 18) - idade))
elif sexo == "feminino":
    print("Pessoas do sexo feminino não precisam fazer o alistamento militar obrigatório.")
