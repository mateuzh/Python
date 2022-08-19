
#Docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: A contagem irá pular de passo em passo
    :return: Não retorna
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print(f'FIM!!!')

#Parâmetro opcional


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma foi {s}')


somar(0, 3, 5)
somar(0, 3)


#Escopo global e local
def teste():
    global n1
    n1 = 5
    print(f'n1 dentro vale {n1}')


n1 = 6
print(f'n1 fora vale {n1}')


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r = []
r.append(soma(3, 4, 8))
print(r)


def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um valor: '))
par(num)
if par(num):
    print(f'É par! ')
else:
    print(f'Não é par!')
