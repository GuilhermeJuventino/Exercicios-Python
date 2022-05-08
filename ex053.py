frase = str(input("Digite uma frase qualquer: ")).strip().upper().replace(" ", "")

for i in range(0, len(frase) + 1):
    inverso = frase[::-1].strip().upper().replace(" ", "")

print(f"O inverso de {frase} é {inverso}")

if inverso == frase:
    print("A frase digitada É UM PALÍNDROMO!")
else:
    print("A frase digitada NÃO É UM PALÍNDROMO!")
