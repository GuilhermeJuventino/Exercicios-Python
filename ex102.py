def fatorial(val, mostrar=False):
    """

    -> Calcula o Fatorial de um valor.
    :param val: O número/valor a ser calculado.
    :param mostrar: (Opcional) Mostrar ou não o passo a passo do calculo.
    :return: O fatorial do valor passado como parametro.
    """
    if not mostrar:
        mostrar = False

    multiplicador = val - 1
    resultado = 0

    print("-" * 29)
    for c in range(1, val):
        if mostrar:

            if multiplicador >= val - 1:
                print(f"{val} x {multiplicador}", end=" ")

            else:
                print(f"x {multiplicador}", end=" ")

        val = val * multiplicador

        if multiplicador >= 1:
            multiplicador -= 1

            resultado = val

    if not mostrar:
        return f"{resultado}"

    else:
        return f"= {resultado}"


# Programa principal
print(fatorial(5))
