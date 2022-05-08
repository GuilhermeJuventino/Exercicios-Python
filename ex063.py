# Sequencia de Fibonacci
# 0-1-1-2-3-5-8-13-21-etc

contador = 0
número_de_termos = int(input("Quantos termos você quer mostrar? "))

anterior = 0
proximo = 1
soma = 1

while contador < número_de_termos:
    print(f"{anterior}", end=" > ")
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
    contador += 1

print("Fim")
