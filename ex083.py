expressão = str(input("Digite uma expressão matemática: ")).strip()
parentesis_a = parentesis_b = 0

for val in expressão:
    if val == "(":
        parentesis_a += 1

    elif val == ")":
        parentesis_b += 1

if parentesis_a == parentesis_b:
    print("Expressão válida.")

else:
    print("Expressão inválida.")
