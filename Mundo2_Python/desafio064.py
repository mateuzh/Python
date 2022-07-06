#Código para leitura de quantos números o usuário desejar com flag de parada sendo '999'

p = 0
p = int(input('Digite um valor: [999 é o número para parar o programa!] '))
c = 0
s = 0

while p != 999:
    c += 1
    s += p
    p = int(input('Digite um valor: [999 é o número para parar o programa!] '))
print(f'{c} foi a quantidade de valores digitados! ')
print(f'{s} foi a soma dos valores digitados! ')
