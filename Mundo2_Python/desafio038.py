#Código para comparar dois valores e dizer qual é o maior ou se os valores são iguais.

v1 = float(input('Digite o primeiro valor: '))
v2 = float (input('Digite o segundo valor: '))
if v1 > v2:
    print (f'O primeiro valor  é o maior!')
elif v2 > v1:
    print (f'O segundo valor é o maior!')
else:
    print (f'Nenhum valor é maior, ambos são iguais.')