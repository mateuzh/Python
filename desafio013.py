'''Código que define quanto será o aumento com base no salário digitado,
com porcentagem de aumenta definida.'''

s = float(input('Informe seu salário: R$'))
au = s*(15/100)
ns = s + au
print (f'Com base em um salário de R${s}, com 15% de aumento, seu novo salário será de R${ns:.2f}')