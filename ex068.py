from random import randint

print("PAR OU ÍMPAR!")

# Conta quantas vezes o jogador venceu.
vitórias = 0

while True:
    # Gerador de número aleatório de 1 até 10.
    randrange = randint(1, 10)

    jogador = int(input("Digite um número: "))

    par_ou_ímpar = str(input("Vai jogar PAR ou ÍMPAR [P/I]: ")).strip().upper()[0]

    if par_ou_ímpar not in "PI":
        continue

    # Faz o computador escolher um número aleatório de 1 até 10.
    computador = randrange
    total = jogador + computador

    print(f"Você jogou {jogador} e o computador {computador}.", end=" ")

    # Determina se o total foi PAR ou ÍMPAR.
    if total % 2 == 0:
        print(f"Total de {total} DEU PAR")
    else:
        print(f"Total de {total} DEU ÍMPAR")

    # Determina se o jogador venceu ou perdeu.
    # Se o jogador vencer, adiciona 1 no contador de vitórias.
    # Se o jogador perder, o jogo acaba.
    if total % 2 == 0 and par_ou_ímpar == "P":
        print("Você venceu! Proxima rodada...")
        vitórias += 1
    elif total % 2 != 0 and par_ou_ímpar == "I":
        print("Você venceu! Proxima rodada...")
        vitórias += 1
    else:
        print("Você perdeu!")
        break

# Mostra quantas vitórias o jogador teve.
print(f"FIM DE JOGO!\nVocê venceu {vitórias} vezes.")
