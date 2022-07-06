#Jogo de Par ou Impar com flag de parada quando o usuário perder

from random import randint

print('~~'*30)
print('Vamos jogar PAR ou IMPAR? ')
print('~~'*30)

jogador = maquina = soma = resultado = quantidade = 0

while True:
    jogador = int(input('Digite um número: '))
    maquina = randint(0, 10)  # Escolhe um valor aleatório para a máquina de 0 a 10
    soma = jogador + maquina
    poi = ' '
    while poi not in 'PI':
        poi = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if poi == 'P':
        if soma % 2 == 0:
            print(f'Você venceu! Eu escolhi {maquina} e você {jogador}!\nVamos jogar novamente...')
            quantidade += 1
            print(f'-=' * 30)
        else:
            print(f'Você perdeu! Eu escolhi {maquina} e você {jogador}!')
            break
    if poi == 'I':
        if soma % 2 == 1:
            print(f'Você venceu! Eu escolhi {maquina} e você {jogador}!\nVamos jogar novamente...')
            quantidade += 1
            print(f'-='*30)
        else:
            print(f'Você perdeu! Eu escolhi {maquina} e você {jogador}!')
            break

print('='*60)
if quantidade == 1:
    print(f'Game over! Você ganhou {quantidade} vez! ')
elif quantidade > 1:
    print(f'Game over! Você ganhou por {quantidade} vezes consecutivas, meus parabéns! ')
elif quantidade == 0:
    print('Game over, parece que você não conseguiu me vencer! ')
