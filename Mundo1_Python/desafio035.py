l1 = float(input('Informe o 1º lado: '))
l2 = float(input('Informe o 2º lado: '))
l3 = float(input('Informe o 3º lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print (f'Os valores acima PODEM formar um triângulo! ')
else:
    print(f'Os valores acima NÃO PODEM formar um triângulo! ')
