matriz = [[], [], []]
contador = index = 0

for c in range(0, 9):
    número = int(input(f"Digite um número para a posição [{index}, {contador}]: "))
    matriz[index].append(número)
    contador += 1

    if contador == 3:
        contador = 0
        index += 1

print(f"[{matriz[0][0]:^5}][{matriz[0][1]:^5}][{matriz[0][2]:^5}]")
print(f"[{matriz[1][0]:^5}][{matriz[1][1]:^5}][{matriz[1][2]:^5}]")
print(f"[{matriz[2][0]:^5}][{matriz[2][1]:^5}][{matriz[2][2]:^5}]")
