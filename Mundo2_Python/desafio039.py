from datetime import date
print('\033[7;40m='*150)
print('\033[7;40m ALISTAMENTO MILITAR - VERIFICAÇÃO PERIÓDICA ')
print('\033[7;40m=\033[m'*150)
anonasc = int(input('    Digite aqui seu ano de nascimento: '))
alist = int(date.today().year - anonasc)
anoalist = anonasc + 18
if alist < 18:
    anosfaltam = 18 - alist
    print(f'''    Ainda não chegou seu momento de se alistar!
    Mas falta(m) {anosfaltam} ano(s) para chegar a sua hora! 
    Seu ano de alistamento é {anoalist}! Não perca o prazo.''')
elif alist == 18:
    print (f'''    Você tem {alist} anos. Seu momento de alistamento chegou! 
    Se apresente a guarnição mais próxima e venha servir o seu país! ''')
elif alist > 18:
    print(f'''    Sua hora já passou soldado! 
    Espero que você já tenha se alistado em {anoalist} e esteja cumprindo ou cumpriu seu dever com a pátria!. ''')