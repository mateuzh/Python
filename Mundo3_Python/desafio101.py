from datetime import datetime


def voto(i):
    atual = datetime.today().year
    idade = atual - i
    if 65 >= idade >= 18:
        return f'Com {idade} anos de idade o voto é OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos de idade AINDA NÃO PODE VOTAR! '
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos de idade o voto é OPCIONAL'


n = int(input(f'Em que ano você nasceu? '))
print(f'{voto(n)} ')
