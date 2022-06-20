from time import sleep
from datetime import date

anoatual = int(date.today().year)
anonasc = int(input('Digite seu ano de nascimento: '))

print('''Vamos verificar em qual categoria você se encaixa.
Verificando... ''')
sleep(0.5)
idade = anoatual - anonasc
if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'
print(f'Você está com {idade} anos e sua categoria é a {categoria}')

