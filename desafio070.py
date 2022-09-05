print('-'*40)
print(' LOJÃO DA ECONOMIA ')
print('-'*40)

nomep = resposta = nomeb = ' '
preço = quantidade = somat = caro = barato = 0

while True:
    nomep = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    somat += preço
    quantidade += 1
    if quantidade == 1 or preço < barato:
        barato = preço
        nomeb = nomep
    if preço > 1000:
        caro += 1
    resposta = str(input('Passar mais produtos? [S/N] '))
    while resposta not in 'SN':
        resposta = str(input('Passar mais produtos? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break

print('-'*40)
print(f'PROGRAMA FINALIZADO! ')
print('-'*40)
print(f'''O valor total da compra ficou em R${somat:.2f}.
Tivemos {caro} produtos com valor superior a R$1.000,00.
O produto com valor mais barato foi {nomeb} custando R${barato}''')
