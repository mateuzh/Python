#código para verificar se uma frase digitada pelo usuário é um palíndromo

frase = str(input('Escreva uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
contrário = junto[::-1]
print(f'O inverso de {frase} é {contrário}')
print('Então... ')
if junto == contrário:
    print('A frase \033[34mÉ\033[m um PALÍNDROMO')
else:
    print('A frase \033[31mNÃO\033[m é um PALÍNDROMO')



