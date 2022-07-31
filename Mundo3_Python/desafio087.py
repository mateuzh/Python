#Código para analisar valores dentro de uma lista que estão dentro de outra lista.

matriz = [[], [], []]
linha = soma = soma3 = m2l = 0 #m2l Maior da segunda linha

for c in matriz:
    for c in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para a posição [{linha}, {c}]: ')))
    linha += 1

linha = 0

print (f'-='*30)

for c in matriz:
    for c in range(0, 3):
        print(f'[  {matriz[linha][c]}  ]', end='')
        if matriz[linha][c] % 2 == 0: #Verifica se o valor dentro da lista é par
            soma += matriz[linha][c]    #Soma o valor se for par
        if c == 2:  #Seleciona a 3ª coluna
            soma3 += matriz[linha][c]   #Soma somente os valores da 3ª coluna
        if linha == 1:  #Seleciona a 2ª linha
            m2l = matriz[linha][c]
            if matriz[linha][c] > m2l: #Verifica o maior valor dentro da 2ª linha
                m2l = matriz[linha][c]
    linha += 1
    print()

print (f'-='*30)

print(f'Valor da soma entre os números pares: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {m2l}')
#print(f'O maior valor da segunda linha é: {max(matriz[1])}')
