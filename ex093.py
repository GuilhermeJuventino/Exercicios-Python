jogador = {}
lista_de_gols = []
total_de_gols = 0

jogador['nome'] = str(input("Nome do jogador: ")).strip().capitalize()
partidas = int(input(f"Quantas partidas jogador {jogador['nome']} jogou? "))

for c in range(0, partidas):
    gols = int(input(f"Quantos gols na partida {c}? "))
    total_de_gols += gols
    lista_de_gols.append(gols)

jogador['gols'] = lista_de_gols
jogador['total'] = total_de_gols

print("-=" * 40)
print(jogador)
print("-=" * 40)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("-=" * 40)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for c in range(0, partidas):
    print(f"    => Na partida {c}, fez {jogador['gols'][c]} gols.")

print(f"Foi um total de {jogador['total']} gols.")
