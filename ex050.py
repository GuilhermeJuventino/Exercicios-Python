soma = 0
cont = 0

for c in range(1, 7):
    número = int(input("Digite um número: "))
    if número % 2 == 0:
        soma = soma + número
        cont = cont + 1
print("A soma de todos os {} números pares é {}.".format(cont, soma))
