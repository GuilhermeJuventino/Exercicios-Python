from datetime import date

ano_atual = date.today().year
c_maior = 0
c_menor = 0

for i in range(1, 8):
    ano = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    if ano_atual - ano >= 21:
        c_maior += 1
    else:
        c_menor += 1

print(f"Ao todo tivemos {c_maior} pessoas maiores de idade\nE também tivemos {c_menor} pessoas menores de idade")
