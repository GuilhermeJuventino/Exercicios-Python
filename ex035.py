print("Analisador de Triângulos")

lado1 = float(input("Primeiro segmento: "))
lado2 = float(input("Segundo segmento: "))
lado3 = float(input("Terceiro segmento: "))

#Determinando se os 3 lados formam um triângulo

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os tres segmentos PODEM formar um triângulo.")
else:
    print("Os tres segmentos NÃO PODEM formar um triângulo.")
