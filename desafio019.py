'''Código que realiza o sorteio de alunos utlizando random.choice'''

from random import choice
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
print (f'O aluno sorteado foi: {sorteio}')