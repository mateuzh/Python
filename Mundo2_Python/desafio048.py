#código para somar números ímpares e múltiplos de três de 1 à 500.

s = 0
n = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        n += 1
        s += c
print(f'A quantidade de números ímpares e múltiplos de 3 é de {n} e a soma de todos eles foi {s}')
