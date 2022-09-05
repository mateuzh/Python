from random import randint

lista = randint(0,10), randint(0, 10), randint(0, 10), \
        randint(0, 10), randint(0, 10)
print(f'Os números sorteados foram :{lista}')
print(f'O maior número sorteado foi {max(lista)} e o menor foi {min(lista)}')
