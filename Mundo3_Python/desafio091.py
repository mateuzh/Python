from time import sleep
from random import randint
from operator import itemgetter

classificação = ()
jogos = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
print(f'== Resultados: ==')
for k, v in jogos.items():
    print(f'{k} tirou {v}')
    sleep(1)
classificação = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(f'-='*20)
print(f'\* Classificação: */')
for k, v in enumerate(classificação):
    print(f'{k+1}ª posição: {v[0]} com {v[1]}')
    sleep(1)