from random import randint
from time import sleep


def sorteio(valores):
    print(f'Sorteando os valores ', end='')
    for c in range(0, 5):
        valores.append(randint(0, 10))
        print(f'{valores[c]} ', end='')
        sleep(0.3)


def somapar(pares):
    soma = 0
    print(f'A soma entre os valores pares da lista {pares} foi: ', end='')
    for c in range(0, len(pares)):
        if pares[c] % 2 == 0:
            soma += pares[c]
    print(f' {soma}')


lista = []
sorteio(lista)
print()
somapar(lista)

