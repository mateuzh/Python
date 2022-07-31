#Código para formar uma matriz.

matriz = [[], [], []]
linha = 0

for c in matriz:
    for c in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para a posição [{linha}, {c}]: ')))
    linha += 1
linha = 0

print('-='*30)

for c in matriz:
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end='')
    linha += 1
    print()
