#Código para inserir listas dentro de dicionários

from time import sleep

inf = dict()
lista = list()
acima = list()
soma = média = 0

while True:
    inf['nome'] = str(input('Nome: '))
    while True:
        inf['sexo'] = str(input('Gênero: [M/F] ')).strip().upper()[0]
        if inf['sexo'] in 'FM':
            break
        print('Resposta inválida. Vamos tentar novamente! ')
    inf['idade'] = int(input('Idade: '))
    soma += inf['idade']
    lista.append(inf.copy())
    while True:
        resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Resposta inválida. Tente novamente')
    if resp in 'N':
        break

for c in range(0, len(lista)):
    if lista[c]['idade'] > média:
        acima.append(lista[c])
média = soma / len(lista)
print(f'->'*40)
print(f'O número de pessoas cadastradas foi: {len(lista)}')
print(f'A média de idade do grupo é de: {média:.2f}')
print(f'A lista de todas as mulheres cadastradas: ', end='')
for m in lista:
    if m['sexo'] in 'Ff':
        print(m['nome'], end=' ')
print( )
print(f'Lista das pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] > média:
        for k, v in p.items():
            print(f' -> {k} = {v};', end='')
        print( )
sleep(1)
print('Programa finalizado! ')
