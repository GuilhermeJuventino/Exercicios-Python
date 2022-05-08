lista_de_alunos = []
notas_do_aluno = []
notas = []
número = 0

while True:
    nome = str(input("Nome: ")).strip().capitalize()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    média = (nota1 + nota2) / 2

    notas_do_aluno.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    notas_do_aluno.append(notas[:])
    notas_do_aluno.append(média)

    lista_de_alunos.append(notas_do_aluno[:])
    notas.clear()
    notas_do_aluno.clear()

    continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

    if continuar == "N":
        break

print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 26)

for i, j in enumerate(lista_de_alunos):
    print(f"{i:<4}{lista_de_alunos[i][0]:<10}{lista_de_alunos[i][2]:>8.1f}")

print("-" * 40)

while número != 999:
    número = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if número == 999:
        break

    else:
        try:
            print(f"As notas de {lista_de_alunos[número][0]} são {lista_de_alunos[número][1]}")
            print("-" * 40)
        except:
            print(f"Erro: Aluno {número} não existe.")
            continue

print("FINALIZANDO...")
print("<<< VOLTE SEMPRE >>>")
