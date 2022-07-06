#Código de jogo de adivinhar em qual número o computador está 'pensando'.

from random import randint

print('\033[31m-'*10, 'TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO', '-'*10)
print('-'*15, 'DICA: O NÚMERO ESTÁ ENTRE 0 E 100 ', '-'*15)

jogador = int(input('Digite sua resposta: '))
computador = randint(0, 100)
cont = 1
while jogador != computador:
    if jogador > computador:
        jogador = int(input(f'Menos... Vamos tentar novamente? '))
    else:
        jogador = int(input(f'Mais... Vamos tentar novamente? '))
    cont += 1
if cont == 1:
    print(f'Caramba! Você acertou de primeira! Meus parabéns! Eu realmente pensei no número {computador}')
else:
    print(f'Parabéns, você acertou! Mas você levou {cont} tentativas para adivinhar que eu pensei no número {computador}! ')



