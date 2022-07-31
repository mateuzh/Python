#Código que informa a quantidade de elementos presentes em uma lista, ordem decrescente e se há um determinado número x na mesma.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Resposta inválida! Tente novamente.\nQuer continuar? [S/N]')).upper().strip()[0]
    if resposta in 'N':
        break

lista.sort(reverse=True)

print(f'A quantidade de valores digitados foi: {len(lista)}')
print(f'Lista digitada em ordem decrescente: {lista}')

if 5 in lista:
    print(f'O número 5 foi encontrado na lista! Na {lista.index(5)}ª posição')
else:
    print(f'O número 5 não foi encontrado na lista!')
