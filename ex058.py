from random import randint
from time import sleep

computador = randint(1, 10)
tentativas = 0

print("Bem vindo ao jogo de adivinhação (v2.0)")
print("O computador (No caso eu) ira pensar em um número de 1 a 10, tente adivinhar!")
print("Pensando...")
sleep(2)

jogador = int(input("Digite um número de 1 a 10: "))
tentativas += 1

if jogador != computador:
    print("Errou!")
    if jogador < computador:
        print("Maior")
    else:
        print("Menor")
    while jogador != computador:
        tentativas +=1
        jogador = int(input("Digite um número de 1 a 10: "))
        if jogador < computador:
            print("Maior")
        elif jogador > computador:
            print("Menor")
        elif jogador == computador:
            print("Acertou!")
            break

print(f"Voce precisou de {tentativas} tentativas para acertar")
