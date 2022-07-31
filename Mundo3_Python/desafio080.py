#Código para ordenar os valores de uma lista sem usar o Sort

números = []

for c in range(0,5):
    new = int(input('Digite um valor: '))
    if c == 0 or new > números[-1]:
        números.append((new))
        print(f'Adicionado ao final da lista! ')
    else:
        pos = 0
        while pos < len(números):
            if new <= números[pos]:
                números.insert(pos, new)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(f'Valores adicionados: {números}')
