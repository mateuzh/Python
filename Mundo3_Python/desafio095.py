jogadores = {}
dados = []
jogos = soma = 0
totalgols = []
resp = escolha = ''

print(f'_'*50)
while True:
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogadores["nome"]} fez? '))
    for c in range(0, jogos):
        gols = int(input(f'Quantos gols {jogadores["nome"]} fez no jogo {c}? '))
        soma += gols
        totalgols.append(gols)
    jogadores['soma'] = soma
    jogadores['gols'] = totalgols[:]
    totalgols.clear()
    dados.append(jogadores.copy())
    soma = 0
    resp = str(input('Continuar? [S/N] '))
    if resp in 'Nn':
        break
    print(f'_'*50)

print(f'_'*50)

print(f'{"Cód":<5} {"Jogador":<12} {"gols":<10} {"soma":>5}')
for c in range(0, len(dados)):
    print(f'{c:<5} {dados[c]["nome"]:<12} {dados[c]["gols"]} {dados[c]["soma"]:>5}')

print(f'_'*50)

while True:
    escolha = int(input('Mostrar dados de qual jogador? '))
    if escolha == 999:
        break
    else:
        print(f'Mostrando dados do jogador {dados[escolha]["nome"]}')
        for k, v in enumerate(dados[escolha]['gols']):
            print(f'No jogo {k} {dados[escolha]["nome"]} fez {v} gols')
