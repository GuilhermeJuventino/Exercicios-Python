número = int(input("Digite um número: "))
cont = 0

for i in range(1, número + 1):
    if número % i == 0:
        print("\033[33m", end=" ")
        cont += 1
    else:
        print("\033[31m", end=" ")
    print(f"{i}", end=" ")

print(f"\n\033[mO número {número} foi divisivel {cont} vezes")

if cont == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
