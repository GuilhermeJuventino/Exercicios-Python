from random import randint

print("Bem vindo ao jogo de adivinhação! nesse jogo você deve adivinhar o numero gerado de 0 a 5.")
número = randint(0, 5)
jogador = int(input("Adivinhe o número (de 0 a 5): "))
print(número)

if jogador == número:
    print("Você venceu!")
else:
    print("Você perdeu!")

