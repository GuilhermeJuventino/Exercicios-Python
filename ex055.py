print("Leitor de pesos: esse programa vai ler o peso de 5 pessoas e dizer qual é o maior e o menor entre elas.")

lista_peso = []

try:
    for c in range(1, 6):
        peso = float(input(f"Digite o peso da {c}ª pessoa: "))
        lista_peso += [peso]
except:
    print("Erro! Digite um número...")
    quit()

print(f"O maior peso lido foi de {max(lista_peso)}Kg")
print(f"O menor peso lido foi de {min(lista_peso)}Kg")
