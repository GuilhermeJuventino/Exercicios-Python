from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}

ranking = {}
colocação = 1

print("Valores sorteados:")
print("-=" * 30)

for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("Ranking:")
print("-=" * 30)

for c in range(0, 4):
    print(f"{colocação} lugar: {ranking[c]}")
    colocação += 1
