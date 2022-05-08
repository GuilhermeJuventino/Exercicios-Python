número = int(input("Digite um número inteiro: "))

conversão = int(input("""Escolha uma das bases para a conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
Sua opção: """))

if conversão == 1:
    print("{} em BINÁRIO é igual a {:b}".format(número, número))
elif conversão == 2:
    print("{} em OCTAL é igual a {:o}".format(número, número))
elif conversão == 3:
    print("{} em HEXADECIMAL é igual a {:X}".format(número, número))
else:
    print("Opção inválida!")
