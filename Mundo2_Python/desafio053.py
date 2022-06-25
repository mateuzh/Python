frase = str(input('Escreva uma frase: ')).strip().upper()
frase = frase.split()
frase = ''.join(frase)
contrário = frase[::-1]
print(contrário)
if frase == contrário:
    print('A frase \033[34mÉ\033[m um PALÍNDROMO')
else:
    print('A frase \033[31mNÃO\033[m é um PALÍNDROMO')



