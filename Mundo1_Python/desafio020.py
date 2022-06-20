'''Código que cria lista em ordem aleatória utilizando random.shuffle'''

from random import shuffle
n1 = str(input('Nome do primeiro aluno(a): '))
n2 = str(input('Nome do segundo aluno(a): '))
n3 = str(input('Nome do terceiro aluno(a): '))
n4 = str(input('Nome do quarto aluno(a): '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print (f'A ordem de apresentação será: \n {lista}')
