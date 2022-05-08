from time import sleep

velocidade = float(input("Qual é a velocidade atual do carro? "))
velocidade_maxima = (velocidade - 80) * 7

print("Processando...")
sleep(3)

print("Sua velocidade atual é de {:.0f}Km/h.".format(velocidade))
if velocidade <= 80:
    print("Você esta dentro do limite de velocidade de 80Km/h, diriga com atenção!")
else:
    print("Você ultrapassou o limite de velocidade de 80Km/h e sera multado!")
    print("Sua multa sera de R${:.2f}!".format(velocidade_maxima))
