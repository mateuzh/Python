#Código para ler o número digitado pelo usuário e mostrá-lo por extenso utilizando tuplas

números = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', \
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', \
          'dezoito', 'dezenove', 'vinte'
while True:
    escolha = int(input('Digite um valor de 0 a 20: '))
    while escolha > 20 or escolha < 0:
        escolha = int(input('Reposta inválida, tente novamente.\nDigite um valor de 0 a 20: '))
    print(f'Você digitou o número {números[escolha]}')
    continuar = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
