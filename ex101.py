def voto(ano):
    import datetime
    ano_atual = datetime.datetime.now().year

    if ano_atual - ano >= 18 and ano_atual - ano < 65:
        return f"Com {ano_atual - ano} anos: VOTO OBRIGATÓRIO."

    elif ano_atual - ano >= 16 and ano_atual - ano < 18 or ano_atual - ano >= 65:
        return f"Com {ano_atual - ano} anos: VOTO OPCIONAL."

    elif ano_atual - ano < 16:
        return f"Com {ano_atual - ano} anos: NÃO VOTA."


# Programa Principal
print("-" * 29)
ano_de_nascimento = int(input("Em que ano você nasceu? "))

print(voto(ano_de_nascimento))
