soma = 0
maioridade = 0
nomehv = 0
nomem = 0

for c in range(1,5):
    nome = str(input(f'{c}ª Pessoa: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Gênero: [Masculino/Feminino] ')).strip().upper()
    print('=-'*14)
    if sexo == 'MASCULINO':
        if c == 1:
            nomehv = nome
            maioridade = idade
        elif idade > maioridade:
            maioridade = idade
            nomehv = nome
    if sexo == 'FEMININO':
        if idade < 20:
            nomem = nomem + 1
    soma = soma + idade
    média = soma / 4

print(f'A média de idade entre o grupo de pessoas foi de: \033[31m{média}\033[m anos de idade. ')
print(f'O nome do homem mais velho do grupo é \033[34m{nomehv}\033[m com \033[34m{maioridade}\033[m anos de idade! ')
print(f'A quantidade de mulheres com menos de 20 anos de idade é de \033[35m{nomem}\033[m')
