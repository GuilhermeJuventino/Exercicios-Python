distância = float(input("Informe a distancia da viagem em Km: "))

print("Você esta prestes a começar uma viagem de {:.1f}Km.".format(distância))

if distância > 200:
    print("O preço da sua viagem sera de R${:.2f}".format(distância * 0.45))
else:
    print("O preço da sua viagem sera de R${:.2f}".format(distância * 0.50))
