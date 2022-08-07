from time import sleep

jogadores = {} #Adiciona os dados temporários digitados para posteriormente ser passado a uma lista
dados = [] #Lista que recebe todos os valores do dicionário temporário jogadores
jogos = soma = 0 #Soma: soma dos gols de um determinado jogador. Jogos: Quantas partidas o jogador fez.
totalgols = [] #Monta a lista de gols feitos
resp = escolha = '' #Validar escolha do usuário, se quer continuar ou não

print(f'_'*50)

while True:
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogadores["nome"]} fez? '))
    for c in range(0, jogos):
        gols = int(input(f'Quantos gols {jogadores["nome"]} fez no jogo {c}? '))
        soma += gols
        totalgols.append(gols) #Lista dos gols
    jogadores['soma'] = soma
    jogadores['gols'] = totalgols[:] #Adiciona a lista dos gols no dicionário que contém os dados dos jogadores
    totalgols.clear() #Apaga os dados temporários dos gols para que sejam colocados novos.
    dados.append(jogadores.copy()) #Passa os valores que estão no dicionário temporário para uma lista final, os guardando para serem mostrados posteriormente.
    soma = 0
    resp = str(input('Continuar? [S/N] '))
    if resp in 'Nn':
        break
    print(f'_'*50)

print(f'_'*50)

print(f'{"Cód":<5} {"Jogador":<12} {"gols":<10} {"soma":>5}')
for c in range(0, len(dados)): #Laço para mostrar os dados dos jogadores em forma de lista
    print(f'{c:<5} {dados[c]["nome"]:<12} {dados[c]["gols"]} {dados[c]["soma"]:>5}')

print(f'_'*50)

while True:
    escolha = int(input('Mostrar dados de qual jogador? '))
    if escolha == 999:
        print(f'Finalizando o programa...')
        sleep(1)
        break
    elif len(dados)-1 < escolha:
        print(f'ERRO! Número digitado não encontrado. Tente novamente.')
    else:
        print(f'=- Mostrando dados do jogador {dados[escolha]["nome"]}')
        for k, v in enumerate(dados[escolha]['gols']):
            print(f'=> No jogo {k} {dados[escolha]["nome"]} fez {v} gols')
    print(f'_'*30)