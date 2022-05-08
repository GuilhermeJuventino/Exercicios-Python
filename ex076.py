lista_de_preços = tuple(("Caderno", 10.25, "Lapis", 2.00, "Estojo", 5.43, "PS4", 4500.25,
                        "Bolacha", 2.35, "Livro", 28.39, "Placa de Vídeo", 2500.28))

print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)

# Organiza os produtos e preços de forma tabular.
for preços in range(0, len(lista_de_preços), 2):
    print(f"{lista_de_preços[preços]:.<30} R${lista_de_preços[preços + 1]}")

print("-" * 40)
