#Código para ler quantos valores o usuário quiser com uma pergunta se o usuário quer continuar utilizando lista

lista = []
r = 'S'
média = soma = quantidade = 0
while r in 'Ss':
    valor = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    soma += valor
    quantidade += 1
    lista += [valor]
média = soma / quantidade
if quantidade == 1:
    print(f'Foi digitado somente {quantidade} valor e a média foi de {média}.')
    print(f'Sendo digitado {quantidade} valor, o maior é o {max(lista)} e o menor é o {min(lista)} ')
elif quantidade > 1:
    print(f'Foram digitados {quantidade} valores e a média entre eles é de {média}')
    print(f'Foram digitados {quantidade}, o maior valor dentre eles é {max(lista)} e o menor é {min(lista)}')
