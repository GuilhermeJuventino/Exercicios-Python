print(f"-" * 15, "Simulador de Caixa Eletrônico", "-" * 15)
# O caixa eletrônico contem cédulas de R$50, R$20, R$10, e R$1.

valor = int(input("Digite o valor a ser sacado R$"))

# Loop que conta quantas cédulas de cada valor foram sacadas.
while True:
    # O loop checa se a divisão inteira do valor sacado pela cédula atual (Exemplo: valor dividido por 50)
    # Se a divisão inteira for maior que zero, o programa vai adicionar o resultado da divisão no total

    if valor // 50 > 0:
        total_cédula = valor // 50
        # Calcular o restante do valor, mostrar a quantidade da cédula atual a ser sacada
        valor = valor - (total_cédula * 50)
        print(f"{total_cédula} cédulas de R$50 foram sacadas")

    # Resetar a contagem de cédulas, e começar o processo de novo, agora usando o restante do valor como base para o calculo.
    total_cédula = 0

    if valor // 20 > 0:
        total_cédula = valor // 20
        valor = valor - (total_cédula * 20)
        print(f"{total_cédula} cédulas de R$20 foram sacadas")

    total_cédula = 0

    if valor // 10 > 0:
        total_cédula = valor // 10
        valor = valor - (total_cédula * 10)
        print(f"{total_cédula} cédulas de R$10 foram sacadas")

    total_cédula = 0

    if valor // 1 > 0:
        total_cédula = valor // 1
        print(f"{total_cédula} cédulas de R$1 foram sacadas")

    break

print(f"-" * 15, "Volte Sempre", "-" * 15)
