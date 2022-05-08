from math import sin, cos, tan, radians

ângulo = float(input("Digite o ângulo: "))
#radians = radians(ângulo)

print("O ângulo de {:.2f} tem o SENO de {:.2f}".format(ângulo, sin(radians(ângulo))))
print("O ângulo de {:.2f} tem o COSSENO de {:.2f}".format(ângulo, cos(radians(ângulo))))
print("O ângulo de {:.2f} tem a TANGENTE de {:.2f}".format(ângulo, tan(radians(ângulo))))
