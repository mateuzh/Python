#Código para ler quantos valores o usuário quiser com uma pergunta se o usuário quer continuar utilizando somente while

r = 'S'
soma = v = cont = maior = menor = 0

while r == 'S':
    v = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
    soma += v
    cont += 1

média = soma / cont

print(f'Você digitou {cont} valores e a média entre eles foi {média}')
print(f'O maior valor digitado foi {maior} e o menor {menor}')
