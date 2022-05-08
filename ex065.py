# Variaveis para guardar a soma entre os valores, a média, e o maior e menor valor digitado.
soma = 0
média = 0
menor_valor = 99999999
maior_valor = 0
contador = 0

# Variavel que serve como gambiarra pra poder iniciar o while loop. (E tambem para interromper o mesmo loop.)
continuar = ""

while continuar != "n":
    número = int(input("Digite um número: "))
    soma += número
    contador += 1

    if número < menor_valor:
        menor_valor = número
    elif número > maior_valor:
        maior_valor = número

    continuar = str(input("Quer continuar? (S/N): ")).lower().strip()

média = soma / contador

print(f"Você digitou {contador} números.")
print(f"A média entre todos os valores digitados foi {média}, o menor valor foi {menor_valor}, e o maior foi {maior_valor}.")
