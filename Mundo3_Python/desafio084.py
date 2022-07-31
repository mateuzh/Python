#Código para analisar dados dentro de uma lista e mostrá-los de acordo com o que foi pedido.

pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    while resposta not in 'SsNn':
        resposta = str(input('Resposta inválida! Tente novamente.\nQuer continuar? [s/n] '))
    if resposta in 'Nn':
        break

if len(pessoas) == 1:
    print(f'Somente {len(pessoas)} pessoa foi cadastrada! ')
elif len(pessoas) > 1:
    print(f'Ao todo foram cadastradas {len(pessoas)} pessoas! ')

print(f'O maior peso foi {maior:.1f}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor:.1f}Kg. Peso de: ', end='')
for p in pessoas:
    if p [1] == menor:
        print(f'[{p[0]}] ', end='')
