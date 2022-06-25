#código para somar números pares dentre 6 valores digitados pelo usuário

s = 0
for c in range(0, 6):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        s = s + valor
print (f'A soma dos números pares foi de: {s}')