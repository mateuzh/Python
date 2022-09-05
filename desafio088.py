from random import randint
from time import sleep

palpite = []
q = 0

print('-'*40)
print('PALPITES PARA A MEGA-SENA')
print('-'*40)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)

for c in range(0, quantidade):
    while len(palpite) < 6:
        núm = randint(0, 60)
        if núm not in palpite:
            palpite.append(núm)
        palpite.sort()
    sleep(1)
    print(f'Jogo {c+1}: {palpite}')
    palpite.clear()
print('-=' * 5, 'BOA SORTE!', '-=' *5)
