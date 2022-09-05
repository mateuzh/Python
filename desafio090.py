#Código para validar a média de um aluno utilizando dicionários

tudo = {}
tudo['Nome'] = str(input('Digite o nome: '))
tudo['Média'] = float(input('Digite a média: '))

if tudo["Média"] >= 7:
    tudo['Situação'] = str'Aprovado'
elif 5 <= tudo["Média"] < 7:
    tudo['Situação'] = 'Recuperação'
else:
    tudo['Situação'] = 'Reprovado'
for k, v in tudo.items():
    print(f'{k} é igual a {v}')
