from random import sample

# Gera uma tupla com cinco números aleatórios.
valores = tuple(sample(range(11), 5))

# Mostra os números gerados na tupla, e depois mostra qual é o maior e o menor entre eles.
print(valores)
print(f"O maior número é {max(valores)}")
print(f"O menor número é {min(valores)}")
