def notas(* nota, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param nota: Uma ou mais notas dos alunos (Aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    print("-" * 36)

    dict_nota = {}
    dict_nota['total'] = len(nota)

    soma = 0

    for c in range(len(nota)):
        soma += nota[c]

        if c == 0:
            dict_nota['maior'] = nota[c]
            dict_nota['menor'] = nota[c]

        else:
            if nota[c] > dict_nota['maior']:
                dict_nota['maior'] = nota[c]

            elif nota[c] < dict_nota['menor']:
                dict_nota['menor'] = nota[c]

        dict_nota['media'] = soma / len(nota)

        if sit:
            if dict_nota['media'] >= 9:
                dict_nota['situação'] = "Ótima"

            elif dict_nota['media'] >= 7:
                dict_nota['situação'] = "Boa"

            elif dict_nota['media'] >= 5:
                dict_nota['situação'] = "Razoavel"

            else:
                dict_nota['situação'] = "Ruim"

    return dict_nota


# Programa principal
resp = notas(5.5, 2.5, 1.5)
print(resp)
