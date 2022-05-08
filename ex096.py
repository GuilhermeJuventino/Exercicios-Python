def calcularArea():
    print("-" * 21)

    largura = float(input("LARGURA (m): "))
    comprimento = float(input("COMPRIMENTO (m): "))

    print(f"A área de um terreno de {largura:.1f} x {comprimento:.1f} é de {largura * comprimento:.1f}m².")


print(" Controle de Terrenos")

calcularArea()
