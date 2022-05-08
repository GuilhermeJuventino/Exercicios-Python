primeiro_termo = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
c = 1

while c <= 10:
    print(primeiro_termo, end="-")
    primeiro_termo += razão
    c += 1

print("Fim!")
