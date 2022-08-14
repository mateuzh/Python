from time import sleep

def contador(c, p, f):
    if p > 0:
        print(f'Contagem de {c} até {f} pulando de {p} em {p} ')
    elif p < 0:
        print(f'Contagem de {c} até {f} pulando de {p-p-p} em {p-p-p}')
    print(c, end=' ')
    if c < f:
        while c < f:
            if p == 0:
                c += 1
            c += p
            print(c, end=' ')
            sleep(0.4)
    else:
        while c > f:
            if p == 0:
                c -= 1
            if p > 0:
                c -= p
            elif p < 0:
                c += p
            print(c, end=' ')
            sleep(0.4)
    print()
    print(f'-=' * 20)


print(f'-='*20)
contador(0, 1, 10)
contador(10, 2, 0)

começo = int(input('Começo: '))
fim = int(input('Fim: '))
passo = int(input('Passo quanto: '))
print(f'-='*20)
contador(começo, passo, fim)
