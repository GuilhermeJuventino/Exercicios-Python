# Guarda números digitados em uma lista e mostra quantos foram digitados.
lista = []

while True:
    número = int(input("Digite um número: "))
    lista.append(número)
    continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]

    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]: ")).strip()[0]

    if continuar in "Nn":
        break

print(f"Você digitou {len(lista)} números.")

# Mostra a lista de números em orderm decrescente.
lista.sort(reverse= True)

print(f"Lista de números digitados em ordem decrescente: {lista}")

# Informa o usuário se o número 5 esta ou não na lista.
if 5 in lista:
    print("O número 5 faz parte da lista.")

else:
    print("O número 5 não faz parte da lista.")
