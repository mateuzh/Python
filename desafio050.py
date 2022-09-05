#código para somar números pares dentre 6 valores digitados pelo usuário

cont = 0
s = 0
for c in range(1, 7):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        s += valor
        cont += 1
print (f'A soma dos números pares foi de: {s}\nPois foram digitados {cont} vezes os números pares')