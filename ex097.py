def escreva(string):
    texto = str(string)

    print("~" * (len(texto) + 4))
    print(texto.center(len(texto) + 4, " "))
    print("~" * (len(texto) + 4))


escreva("Guilherme Juventino")
escreva("Curso de Python no YouTube")
escreva("CeV")
