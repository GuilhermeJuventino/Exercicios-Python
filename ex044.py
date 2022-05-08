print("Bem vindo a loja aleatória!")

preço = float(input("Informe o valor do produto que deseja comprar R$"))
formas_de_pagamento = input("""FORMAS DE PAGAMENTO
[1] á vista (com dinheiro ou cheque)
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual será a forma de pagamento? """)

if formas_de_pagamento == "1":
    print("Sua compra de R${:.2f} a visa em dinheiro/chegue receberá 10% de desconto e o preço total será R${:.2f}.".format(preço, preço - (preço * 10 / 100)))
elif formas_de_pagamento == "2":
    print("Sua compra de R${:.2f} a vista no cartão receberá 5% de desconto e o preço total será R${:.2f}.".format(preço, preço - (preço * 5 / 100)))
elif formas_de_pagamento == "3":
    print("Sua compra será parcelada em 2x de R${:.2f} no cartão SEM JUROS, totalizando R${:.2f}.".format((preço / 2), preço))
elif formas_de_pagamento == "4":
    parcelas = int(input("Quantas parcelas? "))
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(parcelas, (preço * 1.20) / parcelas))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, preço + (preço * 20 / 100)))
else:
    print("Opção invalida!")
