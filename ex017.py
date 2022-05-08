from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
print("A hipotenusa vai medir {:.2f}".format(hypot(cateto_oposto, cateto_adjacente)))
