#Código para separar duas listas que estão dentro de uma.

números = [[], []]

for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)

print(f'-='*40)
números[0].sort()
números[1].sort()

print(f'Os números pares digitados em ordem crescente: {números[p]}')
print(f'Os números ímpares digitados em ordem crescente: {números[p]}')
