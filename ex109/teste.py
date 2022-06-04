import moeda

preço = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}")
print(f"O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}")
print(f"Aumentando em 10%, temos {moeda.aumentar(preço, 10, True)}")
print(f"Diminuindo em 10%, temos {moeda.diminuir(preço, 10, True)}")
