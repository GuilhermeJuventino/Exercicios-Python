from random import sample
from time import sleep

lista_geral = []
lista_de_palpites = []

print("-" * 40)
print("LOTERIA ALEATORIA")
print("-" * 40)

jogos = int(input("Quantos jogos você quer sortear? "))
print(f"-=-=-= Sorteando {jogos} jogos -=-=-=")

for c in range(0, jogos):
    lista_geral.append(sample(range(0, 60), 6))

    lista_geral.sort()
    lista_de_palpites.append(lista_geral[:])
    lista_geral.clear()

    sleep(1)
    print(f"O seu {c + 1}º é {lista_de_palpites[c]}")

print("-=-=-= BOA SORTE -=-=-=")
