nome = str(input("Digite seu nome completo: ")).strip()


print("Seu nome completo é\n{}".format(nome))
print("Seu nome em letras maiúsculas\n{}".format(nome.upper()))
print("Seu nome em letras minúsculas\n{}".format(nome.lower()))
print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
print("Sem contar os espaços, seu nome tem {} letras ao todo".format(len(nome) - nome.count(" ")))
