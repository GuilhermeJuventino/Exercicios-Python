def arquivoExiste(arquivo):
    try:
        a = open(arquivo, "rt")
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, "wt+")
        a.close()

    except:
        print(f"\033[31mErro! Não foi possível criar o arquivo {arquivo}!\033[m")

    else:
        print(f"Arquivo {arquivo} criado com sucesso!")


def lerArquivo(arquivo):
    try:
        a = open(arquivo, "rt")

    except:
        print(f"\033[31mErro! não foi possível ler o arquivo {arquivo}!\033[m")

    else:
        print(a.read())
        a.close()
