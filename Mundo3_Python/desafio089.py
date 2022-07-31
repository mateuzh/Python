#Código para colocar dados dentro de uma lista e mostrar de acordo com o que o usuário digitar.

from time import sleep

tudo = []
dados = []
soma = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('1ª Nota: ')))
    dados.append(float(input('2ª Nota: ')))
    tudo.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resposta not in 'NS':
        resposta = str(input('Resposta inválida! Tente novamente\nQuer continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break

print('-='*15)
print(f'{"Nº":<2} {"Nome":<10} {"Média":<8}')
print(f'_'*30)

for pos, c in enumerate(tudo):
    print(f'{pos:<2} {tudo[pos][0]:<10} {(tudo[pos][1] + tudo[pos][2]) / 2:<8.2f}')

while True:
    aluno = int(input('Gostaria de ver as notas de qual aluno? (999 para parar) '))
    print()
    if aluno == 999:
        break
    if aluno <= len(tudo)+1:
        print(f'As notas de {tudo[aluno][0]} foram {tudo[aluno][1], tudo[aluno][2]}')
        print('='*30)

print(f'FINALIZANDO...')
sleep(1)
print('Volte sempre!! ')
