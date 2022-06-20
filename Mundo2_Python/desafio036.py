from time import sleep
casa = float(input('Digite o valor total da casa: R$'))
salario = float(input('Qual seu salário mensal? R$'))
anos = int(input('Em quantos anos você pretende pagar o empréstimo? '))
prestação = casa / (anos * 12)
porcento =  (salario / 100) * 30
print ('Calculando prestação...')
sleep(2)
if  prestação > porcento:
    print(f'Seu empréstimo foi negado! A prestação ficou em R${prestação:.2f} e ultrapassou 30% do seu salário! ')
elif prestação <= porcento:
    print (f'Parabéns!!! Seu empréstimo foi aprovado! Sua parcela mensal ficará em R${prestação:.2f} sendo paga em até {anos} anos!')
print('Seu atendimento foi finalizado! ')
