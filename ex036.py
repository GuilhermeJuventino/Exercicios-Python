from time import sleep

valor_casa = float(input("Qual é o valor da casa que quer comprar? R$"))
salário = float(input("Qual é o seu salário? R$"))
tempo = int(input("Quantos anos de financiamento? R$"))

prestação = valor_casa / (tempo * 12)

print("Processando...")
sleep(3)

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de R${:.2f}".format(valor_casa, tempo, prestação))

if prestação > (salário * 30 / 100):
    print("{}Empréstimo NEGADO!{}".format("\033[31m", "\033[m"))
else:
    print("{}Empréstimo pode ser CONCEDIDO!{}".format("\033[32m", "\033[m"))
