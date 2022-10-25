def metade(n, f=False):
    if f:
        return f'R${n/2}'
    else:
        return n / 2


def dobro(n, f=False):
    if f:
        return f'R${n*2}'
    else:
        return n * 2


def aumentar(n, f=False):
    if f:
        return f'R${n*1.10}'
    else:
        return n * 1.10


def diminuir(n, f=False):
    if f:
        return f'R${n-((n*13)/100)}'
    else:
        return n - ((n * 13) / 100)


def moeda(n):
    return f'R${n}'


