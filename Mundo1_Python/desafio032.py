from datetime import date
ano = int(input('Quer analisar qual ano? '))
if ano == 0:
    ano = date.today().year
elif ano%4 == 0 and ano%100 != 0 or ano%400 ==0:
    print (f'O ano {ano} é BISSEXTO! ')
else:
    print (f'O ano {ano} NÃO é BISSEXTO! ')