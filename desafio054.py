from datetime import date

anoatual = date.today().year
maioridade = 0
menoridade = 0

for c in range (1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = anoatual - nascimento
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'Tivemos \033[34m{maioridade}\033[m pessoas já atingiram a maioridade! \nEnquanto, \033[31m{menoridade}\033[m pessoas ainda não atingiram a maioridade!')
