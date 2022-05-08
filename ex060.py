#Lendo um input de um número para calcular o Fatorial.
#O Try/Except, gera uma mensagen de erro caso o usuario digite qualquer coisa que não seja um número inteiro
#e fecha o programa
try:
    número = int(input("Digite um número para calcular seu Fatorial: "))
except:
    print("Input inválido.")
    quit()
#O if (assim como o try/except acima) gera uma mensagen de erro e fecha o programa.
#Dessa vez o erro aparece caso o usuario digite um número igual ou abaixo de 0.
if número <= 0:
    print("Input inválido.")
    quit()

multiplicador = número - 1
valor = número

print(f"Calculando {número}! =", end=" ")
print(f"{número} x {multiplicador}", end=" ")
#Loop para calcular o Fatorial que continuara rodando até o multiplicador chegar a 1.
#O multiplicador no caso sendo o número original - 1, no fim de cada repetição o número 1 sera subtraido do multiplicador.
while multiplicador != 1:
    resultado = valor * multiplicador
    valor = resultado
    multiplicador -= 1
    print(f"x {multiplicador}", end=" ")
#Mostrando o resultado na tela
print(f"= {resultado}")
