análise = {}
qtdegols = []
total = 0
análise['nome'] = str(input('Nome do jogador: '))
qtde = int(input('Quantas partidas ele disputou? '))
for c in range(0, qtde):
    qtdegols.append(int(input(f'Quantos gols ele fez na partida {c}: ')))
    total += qtdegols[c]
análise['gols'] = qtdegols[:]
análise['total'] = total
print(f'-='*30)
print(análise)
print(f'-='*30)
for k, v in análise.items():
    print(f'{k} tem o valor {v}')
print(f'-='*30)
print(f'O jogador {análise["nome"]} fez {qtde} partidas')
for c, v in enumerate(qtdegols):
    print(f' => Na partida {c}, fez {v} gols. ')
print(f'Sendo um total de {total} gols')