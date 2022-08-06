from datetime import date

anoatual = date.today().year
dados = {}
dados['Nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = anoatual - nascimento
dados['CTPS'] = int(input('Número da sua carteira de trabalho: (tecle 0 se não tiver)'))
if dados['CTPS'] != 0:
    dados['Admissão'] = int(input('Ano da sua contratação: '))
    dados['Salário'] = float(input('Seu salário: R$'))
    dados['Aposentadoria'] = (dados['Admissão'] + 35) - nascimento
print(f'-='*40)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
