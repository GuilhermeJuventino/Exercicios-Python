# Guarda a lista de palavras numa tupla.
lista_de_palavras = tuple(("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON",
                          "CURSO", "GRATIS", "ESTUDAR", "PRATICAR",
                          "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO"))

# Faz um loop que lê cada palavra na tupla.
for palavra in lista_de_palavras:
    print(f"Na palavra {palavra} temos", end=" ")

    # Checa se cada palavra tem uma vogal, e se a palavra tiver vogais, mostra na tela quais são.
    for letra in palavra.lower():
        if letra in 'aeiou':
            print(f"{letra}", end=" ")

    print()

'''a = [2, 3, 4, 7]
b = a[:]
# Ao fazer um variavel vazia receber uma lista, as duas listas são IGUALADAS!
# Por tanto, ao modificar uma lista, as duas serão alteradas.
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")'''