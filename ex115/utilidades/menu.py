from .leia_dados import leiaInt
from .escreva_dados import escreva
from .arquivos import *

from time import sleep


def menu(arquivo):
    opções = {
        1: "Ver pessoas cadastradas",
        2: "Cadastrar novas pessoas",
        3: "Sair do sistema"
    }

    if not arquivoExiste(arquivo):
        criarArquivo(arquivo)

    escreva("SISTEMA ARQUIVO v1.0")

    escreva("MENU PRINCIPAL")

    rodando = True

    while rodando:
        print("-" * 42)

        for k, v in opções.items():
            print(f"\033[33m{k}\033[m - \033[34m{v}\033[m")

        opção = leiaInt("\033[32mSua opção:\033[m ")

        if opção == 1:
            # Listar conteudo de um arquivo.
            escreva("PESSOAS CADASTRADAS")
            lerArquivo(arquivo)

        elif opção == 2:
            escreva("Opção 2")

        elif opção == 3:
            escreva("Saindo do sistema... Até logo!")
            rodando = False

        else:
            print("\033[31mErro! Digite uma opção válida\033[m")

        sleep(2)
