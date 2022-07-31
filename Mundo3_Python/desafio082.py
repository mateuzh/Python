#Código para separar valores que estão em uma lista em outras listas.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Resposta inválida! Tente novamente!\nQuer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Lista completa: {lista}')
pares.sort()
print(f'Lista dos números pares digitados: {pares}')
impares.sort()
print(f'Lista dos números ímpares digitados: {impares}')
