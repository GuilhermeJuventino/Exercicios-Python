def parOuImpar(n=0):
    if n % 2 == 0:
        return True

    else:
        return False


núm = int(input("Digite um número: "))

if parOuImpar(núm):
    print(f"O número {núm} é par!")

else:
    print(f"O número {núm} é impar!")
