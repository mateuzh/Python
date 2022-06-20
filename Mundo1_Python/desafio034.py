salario = float(input('Digite aqui seu salário: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print (f'Você ganhava R${salario:.2f} e passará a receber R${novo:.2f}!')