print("Gerador de PA.")

c = 1
n = 11
contador = 0

primeiro_termo = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

while c < n:
    print(f"{primeiro_termo}", end=" > ")
    primeiro_termo += razão
    c += 1
    contador += 1

    if c == n:
        print("PAUSA")
        s = int(input("\nQuantos termos deseja mostrar a mais? (digite 0 para sair) "))
        n += s

print("Fim")
print(f"Programa finalizado com {contador} termos mostrados.")
