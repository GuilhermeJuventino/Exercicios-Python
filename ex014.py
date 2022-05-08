print("Conversor de temperaturas v2.0")

Graus_C = float(input("Digite a temperatura em ℃: "))
print("A temperatura atual é de {}℃.".format(Graus_C))
converter = input(("Você deseja converter a temperatura para Fahrenheit ou Kelvin? ")).lower().strip()

if converter == "fahrenheit":
    print("A temperatura atual em graus Fahrenheit é de {}℉.".format(9 * Graus_C / 5 + 32))
elif converter == "kelvin":
    print("A temperatura atual em graus Kelvin é de {}K.".format(Graus_C + 273.15))
