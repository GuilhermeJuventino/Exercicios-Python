time = []
jogador = {}
lista_de_gols = []
total_de_gols = 0
continuar = ""
número_do_jogador = 0


while True:
    jogador['nome'] = str(input("Nome do jogador: ")).strip().capitalize()
    partidas = int(input(f"Quantas partidas jogador {jogador['nome']} jogou? "))

    for c in range(0, partidas):
        gols = int(input(f"Quantos gols na partida {c}? "))
        total_de_gols += gols
        lista_de_gols.append(gols)

    jogador['gols'] = lista_de_gols[:]

    lista_de_gols.clear()

    jogador['total'] = total_de_gols

    total_de_gols = 0

    time.append(jogador.copy())

    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if continuar == 'N':
        break

print("-=" * 40)

print("cod ", end="")

for i in jogador.keys():
    print(f"{i:<15}", end="")

print()
print("-" * 40)

for k, v in enumerate(time):
    print(f"{k:>3} ", end="")

    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()

print("-" * 40)

while True:
    número_do_jogador = int(input("Mostrar dados de qual jogador? (999 para parar) "))

    if número_do_jogador == 999:
        break

    if número_do_jogador >= len(time):
        print(f"Erro! Não existe jogador com o código {número_do_jogador}!")

    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[número_do_jogador]['nome']}:")

        for i in range(0, len(time[número_do_jogador]['gols'])):
            print(f"  No jogo {i} fez {time[número_do_jogador]['gols'][i]} gols.")

    print("-" * 40)

print("<< VOLTE SEMPRE >>")
