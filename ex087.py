matriz = [[], [], []]
contador = index = soma_par = soma_terceira_coluna = 0

for c in range(0, 9):
    número = int(input(f"Digite um número para a posição [{index}, {contador}]: "))
    matriz[index].append(número)
    contador += 1

    if contador == 3:
        contador = 0
        index += 1

print("-=" * 40)
print(f"[{matriz[0][0]:^5}][{matriz[0][1]:^5}][{matriz[0][2]:^5}]")
print(f"[{matriz[1][0]:^5}][{matriz[1][1]:^5}][{matriz[1][2]:^5}]")
print(f"[{matriz[2][0]:^5}][{matriz[2][1]:^5}][{matriz[2][2]:^5}]")
print("-=" * 40)

for l in range(0, 3):
    for n in matriz[l]:
        if n % 2 == 0:
            soma_par += n

        if n == matriz[l][2]:
            soma_terceira_coluna += n

print(f"A soma de todos os valores pares digitados é {soma_par}.")
print(f"A soma de todos os valores da terceira coluna é {soma_terceira_coluna}.")
print(f"O maior valor digitado na segunda linha é {max(matriz[1])}.")
