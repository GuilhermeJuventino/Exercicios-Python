from time import sleep

print("Analisador de Triângulos v2.0")

print("Digite o valor dos 3 segmentos do seu triângulo.")

lado1 = float(input("Primeiro segmento: "))
lado2 = float(input("Segundo segmento: "))
lado3 = float(input("Terceiro segmento: "))

print("Processando...")
sleep(1)

if lado3 <= lado1 + lado2 and lado2 <= lado1 + lado3 and lado1 <= lado2 + lado3:
    print("Os 3 segmentos PODEM formar um triângulo", end=" ")
    if lado1 == lado2 == lado3:
        print("EQUILÁTERO!")
    elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os 3 segmentos NÃO PODEM formar um triângulo!")
