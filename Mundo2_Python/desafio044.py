#Programa simulador de sistema de pagamento
print('\033[7;40m=\033[m'*150)
print('\033[7;40mFINALIZAÇÃO DA COMPRA - MEIO, MODO E REGISTRO DE PAGAMENTO')
print('\033[7;40m=\033[m'*150)
vp = float(input('Valor do produto: R$'))
fp = input('Forma de pagamento:\n [1] - Cartão \n [2] - Cheque \n [3] - Dinheiro \n ')

if fp == '1':
    pc = input('\033[7;40mGostaria de parcelar em até quantas vezes? \n (1)Crédito à vista \n (2)2x \n +3x(Digite a quantidade de parcelas (até 24x) ) \033[m \n ')
    if pc == '1':
        vd = vp - ((vp/100)*5)
        print (f' Valor a ser pago com desconto de 5% por ser pagamento à vista no cartão. \n Valor final: R${vd:.2f}')
    elif pc == '2':
        print (f' Valor a ser pago será em condições normais sem desconto por ser parcelado em 2x no cartão. \n Valor final: R${vp:.2f}')
    elif pc >= '3' or pc < '25':
        va = vp + ((vp/100)*20)
        print(f' Valor a ser pago com acréscimo de 20% de juros por ser parcelado em 3x ou mais. \n Valor a ser pago: R${va:.2f} em {pc}x de R${va/int(pc):.2f}')
elif fp == '2' or '3':
    vd = vp - ((vp/100)*10)
    print(f'\033[7;40m Valor a ser pago com desconto de 10% por ser pagamento à vista no dinheiro ou cheque. \n Valor final: R${vd:.2f}')

