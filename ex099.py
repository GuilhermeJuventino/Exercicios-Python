from time import sleep


def maior(*valores):
    print("-=" * 40)
    print("Analizando os valores passados...")
    sleep(0.7)

    if not valores:
        sleep(0.4)
        print(f"Foram informados 0 valores ao todo.")
        print(f"O maior valor informado foi 0.")

    elif len(valores) < 2 and valores[0] == 0:
        print(f"Foram informados 0 valores ao todo.")
        print(f"O maior valor informado foi 0.")
        sleep(0.4)

    else:
        for v in valores:
            sleep(0.4)
            print(f"{v}", end=" ")

        sleep(0.4)
        print(f"Foram informados {len(valores)} valores ao todo.")
        print(f"O maior valor informado foi {max(valores)}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()
