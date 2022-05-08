from time import sleep

número = int(input("Digite um número: "))

print("Processando...")
sleep(2)

if número % 2 == 0:
    print("{} é um número par!".format(número))
else:
    print("{} é um número impar!".format(número))
