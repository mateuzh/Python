#Programa para cadastro de quantas pessoas o usuário quiser

print('PROGRAMA PARA CADASTRO DE PESSOAS')
print('='*40)

maior = qhomem = qmulher20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Gênero: [F/M] ')).strip().upper()[0]
    print('-'*40)
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Resposta inválida!\nGênero: [F/M] ')).upper()[0]
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        qhomem += 1
    if sexo == 'F' and idade < 20:
        qmulher20 += 1
    resposta = str(input('Cadastrar mais pessoas? [S/N] ')).upper().strip()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Resposta inválida!\nCadastrar mais pessoas? [S/N] ')).upper().strip()[0]
    if resposta in 'Nn':
        break

print('='*40)
print(f'''No total, foram cadastrados {maior} pessoas com mais de 18 anos de idade;
Total de {qhomem} homens cadastrados;
E total de {qmulher20} cadastradas mulheres com menos de 20 anos de idade! ''')
