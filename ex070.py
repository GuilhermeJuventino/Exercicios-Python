mais_barato = ""
total = acima_de_1000 = menor_preço = contador = 0

while True:
    nome_produto = str(input("Nome do produto: ")).strip().capitalize()
    preço = int(input("Preço do produto R$"))
    contador += 1
    total += preço

    if preço >= 1000:
        acima_de_1000 += 1
    # Determina o nome do produto mais barato.
    if contador == 1 or preço < menor_preço:
        menor_preço = preço
        mais_barato = nome_produto

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if continuar == "N":
        break

print(f"O total da compra foi R${total:.2f}\nTemos {acima_de_1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {mais_barato} que custou R${menor_preço:.2f}")
