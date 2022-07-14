import urllib
import urllib.request
import urllib.error


def acessarSite(link):
    """Pega um endereço de site digitado pelo o usuário
    e tenta acessa-lo.

    :param link: Endereço do site
    :return: (Sem Retorno)
    """
    texto = str(input(link)).strip().lower()

    endereço = texto

    try:
        site = urllib.request.urlopen(f"https://www.{endereço}/")

    except urllib.error.URLError:
        print("-" * 50)
        print(f"\033[31mERRO! não foi possível acessar o site {endereço}\033[m")
        print("-" * 50)

    else:
        print("-" * 40)
        print(f"\033[34mSite {endereço} acessado com sucesso\033[m")
        print("-" * 40)
