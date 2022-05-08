try:
    número_1 = int(input("Primeiro valor: "))
    número_2 = int(input("Segundo valor: "))
except:
    print("Opção inválida. Por favor, digite um número...")
    quit()
maior = 0

opção = ""

while opção != "5":
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    opção = str(input("Qual é sua opção? "))
    if opção == "1":
        print(f"A soma entre {número_1} + {número_2} é {número_1 + número_2}")
    elif opção == "2":
        print(f"O resultado de {número_1} x {número_2} é {número_1 * número_2}")
    elif opção == "3":
        if número_1 > número_2:
            maior = número_1
        elif número_2 > número_1:
            maior = número_2
        print(f"Entre {número_1} e {número_2} o maior valor é {maior}")
    elif opção == "4":
        try:
            número_1 = int(input("Primeiro valor: "))
            número_2 = int(input("Segundo valor: "))
        except:
            print("Opção inválida. Por favor, digite um número.")
            continue
    elif opção == "5":
        print("Finalizando programa...")
    else:
        print("Opção inválida. Tente novamente.")

print("Fim do programa.")
