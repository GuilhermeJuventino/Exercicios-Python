aluno = {"nome": str(input("Digite o seu nome: ").strip().capitalize())}
aluno["média"] = float(input("Digite sua média: "))

if aluno["média"] >= 7:
    aluno["situação"] = "aprovado"

elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "recuperação"

else:
    aluno["situação"] = "reprovado"

for k, v in aluno.items():
    print(f"{k}: {v}")
