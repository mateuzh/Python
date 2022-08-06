tudo = {}
tudo['Nome'] = str(input('Digite o nome: '))
tudo['Média'] = float(input('Digite a média: '))

if tudo["Média"] >= 6:
    tudo['Situação'] = str('Aprovado')
else:
    tudo['Situação'] = str('Reprovado')
for k, v in tudo.items():
    print(f'{k} é igual a {v}')
