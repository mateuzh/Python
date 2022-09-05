#Adicionando valores à uma lista, porém não adiciona quando o valor já foi digitado

valores = []

while True:
    novovalor = int(input('Digite um valor: '))
    if novovalor not in valores:
        valores.append(novovalor)
        print(f'Valor adicionado com sucesso! ')
    else:
        print(f'Valor duplicado! Não será adicionado! ')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Resposta inválida!\nQuer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break

print(f'-'*40)
print(f'Você digitou os valores {sorted(valores)}')
