
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: Número a ser calculado o fatorial
    :param show: (Opcional) Mostra o passo a passo do fatorial
    :return: O valor do fatorial do número num
    """
    print(f'_'*40)
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == True:
        for c in range(num, 0, -1):
            print(f'{c}', end=' x ' if c != 1 else ' = ')
    return f


print(fatorial(5, show=True))
help(fatorial)
