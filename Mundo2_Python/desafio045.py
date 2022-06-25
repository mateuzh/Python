#Jogo de Jokenpô

from random import choice
from time import sleep

resposta = input('Vamos jogar Pedra, Papel e Tesoura? \nPara SIM tecle [1] \nPara NÃO tecle [2]\nSua opção:')

if resposta == '1':
    print('Pedra...')
    sleep(1)
    print('Papel...')
    sleep(1)
    print('Tesoura...')
    sleep(1)
    jogador = str(input('Sua escolha: ')).upper().strip()
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = choice(lista)
    print(f'Eu escolhi... {computador}!!!')
    if jogador == computador:
        print(f'Empatamos :/! Você escolheu {jogador},e eu escolhi {computador} também!')
    elif jogador == 'PEDRA' and computador == 'TESOURA':
        print (f'Você venceu! {jogador} ganha de {computador}!')
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        print(f'Você venceu! {jogador} ganha de {computador}!')
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        print(f'Você venceu! {jogador} ganha de {computador}!')
    elif jogador == 'PEDRA' and computador == 'PAPEL':
        print (f'Parece que eu venci! {computador} ganha de {jogador}!')
    elif jogador == 'PAPEL' and computador == 'TESOURA':
        print(f'Parece que eu venci! {computador} ganha de {jogador}')
    elif jogador == 'TESOURA' and computador == 'PEDRA':
        print(f'Parece que eu venci! {computador} ganha de {jogador}')
    else:
        print('Sua opção foi inválida! ')
else:
    print('Então não jogamos, finalizando o programa. ')