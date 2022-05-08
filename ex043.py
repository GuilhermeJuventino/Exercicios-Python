peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

IMC = peso / (altura * altura)

print("Seu IMC (Índice de Massa Corporal) é de {:.1f}".format(IMC))

if IMC < 18.5:
    print("Você está ABAIXO DO PESO NORMAL!")
elif IMC >= 18.5 and IMC < 24.9:
    print("Você está na faixa de peso NORMAL!")
elif IMC >= 25 and IMC < 29.9:
    print("Você está ACIMA DO PESO NORMAL!")
elif IMC >= 30 and IMC < 39.9:
    print("Você está em OBESIDADE!")
else:
    print("Você está em OBESIDADE MÓRBIDA!")
