'''Conversor de real para dólar com cotação pre-definida.'''

real = float(input('Quantos reais você têm? R$'))
dolar = real / 4.82
euro = real / 5.13
print (f'Com R${real:.2f} reais você consegue comprar U${dolar:.2f} dolares! E €{euro:.2f} Euros ')