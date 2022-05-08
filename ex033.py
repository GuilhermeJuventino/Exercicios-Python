primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))
terceiro_valor = int(input("Terceiro valor: "))

maior_valor = primeiro_valor
menor_valor = primeiro_valor

# Verificando qual número é menor
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor_valor = segundo_valor
if terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
    menor_valor = terceiro_valor
# Verificando qual número é maior
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior_valor = segundo_valor
if terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    maior_valor = terceiro_valor

print("O menor número digitado foi {}\nO maior número digitado foi {}".format(menor_valor, maior_valor))
