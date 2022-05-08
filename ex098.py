from time import sleep


def contador(i, f, p):
    print("-=" * 20)

    if p == 0:
        p = 1

    p = abs(p)

    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)

    cont = i

    if i < f:

        while cont <= f:
            print(cont, end=" ")
            sleep(0.5)

            cont += p

    else:

        while cont >= f:
            print(cont, end=" ")
            sleep(0.5)

            cont -= p

    print("FIM!")


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print("-=" * 20)
print("Agora é a sua vez de personalizar a contagem!")

ini = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(ini, fim, passo)
