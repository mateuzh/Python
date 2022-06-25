from datetime import date

anoatual = date.today().year
maioridade = 0
menoridade = 0

for c in range (0, 7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = anoatual - nascimento
    if idade >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print(f'\033[34m{maioridade}\033[m pessoas já atingiram a maioridade! \nEnquanto, \033[31m{menoridade}\033[m pessoas ainda não atingiram a maioridade!')