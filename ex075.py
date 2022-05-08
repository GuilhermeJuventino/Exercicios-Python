lista_de_números = tuple((int(input("Digite um número: ")) for c in range(1, 5)))

contador_9 = 0
contador_par = 0

for números in lista_de_números:
    if números == 9:
        contador_9 += 1

print(f"Você digitou os valores {lista_de_números}")

if contador_9 > 1:
    print(f"Você digitou {contador_9} vezes o número 9")
elif contador_9 == 1:
    print(f"Você digitou {contador_9} vez o número 9")

if 3 in lista_de_números:
    print(f"A primeira instancia do número 3 esta na {lista_de_números.index(3) + 1}ª posição")

for números in lista_de_números:
    if números % 2 == 0:
        print(f"{números}", end=" ")
