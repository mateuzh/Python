inf = {}
lista = list()
listam = list()
acima = list()
soma = média = 0

while True:
    inf['nome'] = str(input('Nome: '))
    inf['sexo'] = str(input('Gênero: [M/F] ')).strip()
    if inf['sexo'] not in 'FfMm':
        inf['sexo'] = str(input('Resposta inválida. Vamos tentar novamente\nGênero: [M/F] '))
    inf['idade'] = int(input('Idade: '))
    lista.append(inf.copy())
    resp = str(input('Continuar? [S/N] ')).strip()
    if resp not in 'SsNn':
        resp = str(input('Resposta inválida. Tente novamente\nContinuar? [S/N] '))
    if resp in 'Nn':
        break

for c in range(0, len(lista)):
    soma += lista[c]['idade']
    média = soma / len(lista)
    if lista[c]['sexo'] in 'Ff':
        listam.append(lista[c]['nome'])
for c in range(0, len(lista)):
    if lista[c]['idade'] > média:
        acima.append(lista[c])

print(f'->'*40)
print(f'O número de pessoas cadastradas foi: {len(lista)}')
print(f'A média de idade do grupo é de: {média}')
print(f'A lista de todas as mulheres cadastradas: {listam}')
if len(acima) == 0:
    print(f'Não houve cadastro de pessoas com idade acima da média do grupo!')
for c in range(0, len(acima)):
    print(f'Nome = {acima[c]["nome"]}; Sexo = {acima[c]["sexo"]}; Idade = {acima[c]["idade"]}')
