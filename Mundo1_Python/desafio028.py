from random import randint
from time import sleep
print ('Vou pensar em um número de 0 a 5 e quero que você tente advinhar! ')
print ('='*13, 'PENSANDO', '='*13)
numero = int(input('Qual número você acha que é? '))
print ('PENSANDO...')
sleep(3)
sorteio = randint(0, 5) #faz o computador "Pensar"
if numero == sorteio:
    print(f'Parabéns, você acertou, pensei no número {sorteio}! Como você fez isso? ')
else:
    print(f'Humm, eu pensei no número {sorteio}, você errou! :(')