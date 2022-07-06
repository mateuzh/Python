#Código para mostrar até qual termo de uma PA o usuário quer ver

termo1 = int(input('Digite o primeiro termo da pa: '))
razao = int(input('Digite a razão: '))
r = int(input('Gostaria de ver até qual termo? '))
qtdetermo = termo1+(r-1)*razao
contador = termo1 - razao
mais = ''
total = 0
while r != 0:
    while contador < qtdetermo:
        total += 1
        contador += razao
        print(contador, end=' ')
        print('-> ' if contador < qtdetermo else ' -> PAUSA! =', end=' ')
    r = int(input('Quer ver mais quantos termos? '))
    termo1 = contador
    qtdetermo = termo1+(r)*razao
    while qtdetermo < termo1:
        contador += razao
        print(contador, end='')
        print(' PAUSA ')

print(f'Progressão finalizada com {total} termos mostrados.')
