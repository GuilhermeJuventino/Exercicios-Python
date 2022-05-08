lista_de_números = []
continuar = ""

while True:
    número = int(input("Digite um valor: "))

    # Checa se o valor digitado ja existe na lista, se ele não estiver na lista ele sera adicionado
    # Do contrario o valor duplicado não sera adicionado.
    if número not in lista_de_números:
        lista_de_números.append(número)
        print("Valor adicionado com sucesso.")
    else:
        print("Esse valor ja existe na lista e não sera adicionado.")

    # Checa se o usuário quer continuar ou não
    continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]

    while continuar not in "SsNn":
        # O programar ficara repetindo essa pergunta até o usuário digitar "S" ou "N"
        # (Pode ser tanto em letra maiúscula ou minúscula)
        continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]

    if continuar == "N" or continuar == "n":
        break

print(f"O valores digitados (Em ordem crescente) são...")

# Mostra a lista de valores digitados em ordem crescente.
for chave, valor in enumerate(sorted(lista_de_números)):
    print(f"{valor}... ", end="")

print("\nFim")
