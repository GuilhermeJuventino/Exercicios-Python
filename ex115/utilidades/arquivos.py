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
        for linha in a:
            dados = linha.split(":")
            dados[1] = dados[1].replace("\n", "")
            print(f"{dados[0]:<30}{dados[1]:>3} anos")

        a.close()


def editarArquivo(arquivo, texto):
    try:
        a = open(arquivo, "a")

    except:
        print(f"\033[31mErro! não foi possível abrir o arquivo {arquivo}!\033[m")

    else:
        t = f"{texto}\n"

        try:
            a.write(t)

        except:
            print(f"\033[31mErro! não foi possível editar o arquivo {arquivo}!\033[m")

        else:
            a.close()
