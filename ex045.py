from random import choice
print("Pedra Papel e Tesoura")

print("""Suas opções
PEDRA
PAPEL
TESOURA""")
opções = ["PEDRA", "PAPEL", "TESOURA"]
jogada = str(input("Qual será sua jogada? ")).strip().upper()

computador = choice(opções)

print("Você jogou {}".format(jogada))
print("O computador jogou {}".format(computador))

if jogada == "PEDRA" and computador == "TESOURA":
    print("\033[4:32mVocê ganhou!\033[m")
elif jogada == "PAPEL" and computador == "PEDRA":
    print("\033[4:32mVocê ganhou!\033[m")
elif jogada == "TESOURA" and computador == "PAPEL":
    print("\033[4:32mVocê ganhou!\033[m")
elif computador == jogada:
    print("EMPATE!")
else:
    print("\033[4:31mVocê perdeu!\033[m")
