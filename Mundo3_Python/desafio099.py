def maior(num):
    print(f'Analisando os valores passados... ')
    for c, n in enumerate(num):
        print(n, end=' ')
        if c == 0 or n > big:
            big = n
    print(f'. Foram digitados ao todo {len(num)} ao todo.\nO maior valor digitado foi {big}.')
    print(f'-='*20)

print(f'-=' * 20)
numeros = (2, 3, 6, 9)
maior(numeros)
numeros = (2, 3, 6, 10)
maior(numeros)
