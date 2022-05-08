# Variavel usada para receber os inputs do usuário no loop.
número = 0
# Variavel que conta quantos números foram digitados.
contador = 0
soma = 0

# Loop que lê números inteiros digitados pelo o usuário até ele digitar 999. (Que é a condição de parada.)
# O loop tambem vai somar todos os números digitados e adicionar 1 no contador cada vez que o usuário digitar um número.
while número != 999:
    número = int(input("Digite um número. (999 para parar) "))
    soma += número
    contador += 1

# Print formatado que mostra quantos números o usuário digitou. (Desconsiderando o flag que é 999.)
# E a mostra a soma entre todos os números. (Tambem desconsiderando o flag de 999.)
print(f"Você digitou {contador - 1} números, e a soma entre eles é {soma - 999}")
