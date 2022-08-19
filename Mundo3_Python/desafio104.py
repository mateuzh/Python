

def leiaInt(a):
    while a.isnumeric() != True:
        a = input('Digite um valor: ')
        if a.isnumeric() == True:
            break
        else:
            print(f'\033[31mErro! São aceitos somente números inteiros\033[m ')
    return a


n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')
