import moeda

preço = float(input("Digite o preço: R$"))

print(f"A metade de R${preço} é R${moeda.metade(preço)}")
print(f"O dobro de R${preço} é R${moeda.dobro(preço)}")
print(f"Aumentando em 10%, temos R${moeda.aumentar(preço, 10)}")
print(f"Diminuindo em 10%, temos R${moeda.diminuir(preço, 10)}")
