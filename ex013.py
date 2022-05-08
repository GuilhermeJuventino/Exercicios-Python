preço = float(input("Digite o preço do produto R$"))
vista = preço - (preço * 15 / 100)
parcelado = preço + (preço * 15 / 100)

print("A vista o produto recebe um desconto de 15%, e passa a custar R${:.2f}".format(vista))
print("Parcelado o produto recebe um aumento de 15%, e o preço total das parcelas vira R${:.2f}".format(parcelado))