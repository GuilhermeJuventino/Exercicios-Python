qualificados = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
                'Corinthians', 'Fortaleza',
                'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
                'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

cinco_primeiros = qualificados[0:5]
quatro_últimos = qualificados[-4:]
qualificados_ordem_alfabética = sorted(qualificados)
chapecoense = qualificados.index("Chapecoense")

print(f"Os 5 primeiros colocados são\n{cinco_primeiros}")
print(f"-"*60)

print(f"Os quatro últimos colocados são\n{quatro_últimos}")
print(f"-"*60)

print(f"Qualificados em ordem alfabética\n{qualificados_ordem_alfabética}")
print(f"-"*248)

print(f"A Chapecoense está na {chapecoense + 1}ª posição")
