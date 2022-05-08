números_por_extenso = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
                       "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito",
                       "Dezenove", "Vinte")

while True:
    número = int(input("Digite um número de 0 até 20: "))

    if número < 0 or número > 20:
        print("Erro: Digite um número de de 0 até 20:")
        continue

    print(f"Você digitou o número {números_por_extenso[número]}")

    continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]

    if continuar == "N":
        break

print("Fim do programa...")
