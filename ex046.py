from time import sleep

faltam = int(input("Quantos segundos faltam para a queima de fogos de artifício? "))
for c in range(faltam, -1, -1):
    print(c)
    sleep(1)
print("A queima de fogos começou!")
