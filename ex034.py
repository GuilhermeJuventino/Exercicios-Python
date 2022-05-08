salário = float(input("Digite o seu salário: "))

if salário <= 1250.00:
    print("Você recebeu um aumento de 15%, seu salário agora é de R${:.2f}".format(salário + salário * 15 / 100))
else:
    print("Você recebeu um aumento de 10%, seu salário agora é de R${:.2f}".format(salário + salário * 10 / 100))
