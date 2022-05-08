from time import sleep

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

média = (nota1 + nota2) / 2

print("Processando...")
sleep(2)

print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, média))

if média >= 7.0:
    print("O aluno está {}APROVADO{}.".format("\033[4:32m", "\033[m"))
elif média >= 5.0 and média < 6.9:
    print("O aluno está em RECUPERAÇÃO.")
elif média < 5.0:
    print("O aluno está {}REPROVADO{}.".format("\033[4:31m", "\033[m"))
