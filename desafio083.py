#Código para validar uma expressão, a expressão só será válida caso todos os parenteses sejam fechados

expressão = str(input('Digite sua expressão: '))
lista = []

for simb in expressão:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print(f'Sua expressão está válida! ')
else:
    print(f'Sua expressão está inválida! ')
