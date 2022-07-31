#Código que o usuário insira valores em uma lista

valores = []

for c in range(0,5):
    valores.append(int(input(f'Digite o {c}º valor: ')))

print(f'O maior valor digitado foi {max(valores)} e o menor foi {min(valores)}! ')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for posmaior, v in enumerate(valores):
    if max(valores) == v:
        print(f'{posmaior}...', end=' ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for posmenor, vm in enumerate(valores):
    if min(valores) == vm:
        print(f'{posmenor}...', end=' ')
