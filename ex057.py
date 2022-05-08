sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()

if sexo == "M":
    str(print(f"Sexo {sexo} registrado com sucesso"))
elif sexo == "F":
    str(print(f"Sexo {sexo} registrado com sucesso"))
else:
    while "M" not in sexo or "F" not in sexo:
        sexo = str(input("Dados inválidos. Por favor, digite o seu sexo: ")).upper().strip()
        if sexo == "M":
            str(print(f"Sexo {sexo} registrado com sucesso"))
            break
        elif sexo == "F":
            str(print(f"Sexo {sexo} registrado com sucesso"))
            break
