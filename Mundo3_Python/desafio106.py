from time import sleep
from random import randint


def sistema(f):
    cor = randint(40, 45)
    print(f'\033[{cor}m_'*(len(f)+4))
    print(f'{f}')
    print(f'_'*(len(f)+4))
    print("\033[m")


def sos(resp):
    while resp not in 'fim':
        sistema(f'  Acessando o manual de controle do {resp}')
        help(resp)
        sistema('  SISTEMA DE AJUDA PyHELP')
        resp = str(input('Biblioteca ou função > '))
    print(f'Finalizando...')
    sleep(1)


sos(str(input(f'{sistema("SISTEMA DE AJUDA PyHELP")}\nBiblioteca ou função >')))
