from random import randrange
from time import sleep

lista_núm = []


def sorteia(lst):
    # precisa de uma lista como parametro
    print("Sorteando 5 valores da lista:", end=" ")

    for n in range(0, 5):
        núm = randrange(0, 10)
        sleep(0.4)
        print(f"{núm}", end=" ")
        lst.append(núm)

    print("PRONTO!")


def somaPar(lst):
    # precisa de uma lista como parametro
    soma = 0
    print(f"Somando os valores pares de {lst}, temos", end=" ")

    for n in lst:
        if n % 2 == 0:
            soma += n

    print(soma)


sorteia(lista_núm)
somaPar(lista_núm)
