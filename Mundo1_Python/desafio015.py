'''Código que calcula quanto será pago em aluguel de carro
com valores pre-definidos.'''

dias = int(input('Quantos dias você ficou com o carro? '))
km = float (input('Quantos quilometros você rodou? '))
aluguel = (dias * 60) + (km * 0.15)
print (f'O preço a pagar será de : {aluguel}')