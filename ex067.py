print("Tabuada V3.0!")

while True:
    número = int(input("Digite um número para ver sua tabuada: "))

    if número <= 0:
        break

    for i in range(1, 11):
        print(f"{número} x {i} = {número * i}")

    continuar = str(input("Digite qualquer coisa para continuar. (Ou 'N' para parar.): ")).upper().strip()

    if continuar == "N":
        break

print("Acabou...")
