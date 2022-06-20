l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print(f'Os comprimentos digitados podem formar um triângulo! ')
    if l1 and l2 == l3 and l2 and l3 == l1 and l3 and l1 == l2:
        print (f'E o triângulo é \033[33m equilatero \033[m ! Pois todos os lados são iguais! ')
    elif l1 and l2 == l3 or l2 and l3 == l1 or l3 and l1 == l2:
        print(f'E o triângulo é \033[33m isósceles \033[m! Pois dois lados são iguais. ')
    elif l1 and l2 != l3 and l2 and l3 != l1 and l3 and l1 != l2:
        print (f'E o triângulo é \033[033m escaleno \033[m ! Pois todos os lados são diferentes. ')
else:
    print(f'Os valores não podem formar um triângulo! ')