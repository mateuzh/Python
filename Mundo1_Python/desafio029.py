velocidade = float(input('Qual a velocidade do carro? '))
print ('*'*20, 'VELOCIDADE LIMITE DE 80 KM/H', '*'*20)
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f'Você foi multado em R${multa:.2f}, pois sua velocidade foi {velocidade:.0f}KM/H.')
else:
    print (f'Sua velocidade foi {velocidade:.0f}KM/H, considerada normal para a via.')
print ('Dirija com segurança!')