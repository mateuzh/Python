#Código para colocar uma lista dentro de um dicionário e mostrar os dados.

análise = {}
qtdegols = []

análise['nome'] = str(input('Nome do jogador: '))
jogos = int(input('Quantas partidas ele disputou? '))
for c in range(0, jogos):
    qtdegols.append(int(input(f'Quantos gols ele fez na partida {c}: ')))
análise['gols'] = qtdegols[:]
análise['total'] = sum(qtdegols)
print(f'-='*30)
print(análise)
print(f'-='*30)
for k, v in análise.items():
    print(f'{k} tem o valor {v}')
print(f'-='*30)
print(f'O jogador {análise["nome"]} fez {jogos} partidas')
for c, v in enumerate(análise["gols"]):
    print(f' => Na partida {c}, fez {v} gols. ')
print(f'Sendo um total de {análise["total"]} gols')
