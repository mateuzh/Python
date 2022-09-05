print('-'*65)
print('Escreva dois valores que te darei a opção do que fazer com eles. ')
print('-'*65)
vum = int(input('Digite o 1º valor: '))
vdois = int(input('Digite o 2º valor: '))

menu = 0 #escolha do menu
soma = 0 #soma
m = 0 #multiplicação
maior = vum #maior valor
menor = 0 # menor valor

while menu != 5:
    menu = int(input('''Digite sua escolha: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Sua resposta: '''))
    if menu == 1:
        soma = vum + vdois
        print(f'A soma entre {vum} + {vdois} é de: {soma}\n')
    elif menu == 2:
        m = vum * vdois
        print(f'O valor da multiplicação entre {vum} x {vdois} é de: {m}\n')
    elif menu == 3:
        if maior < vdois:
            maior = vdois
        else:
            maior = vum
        print(f'O maior valor entre {vum} e {vdois} foi: {maior}\n')
    elif menu == 4:
        vum = int(input('Digite o novo 1º valor: '))
        vdois = int(input('Digite o novo 2º valor: '))
        print(' ')
    elif menu == 5:
        print(f'Finalizando o programa... ')
    else:
        print('Opção inválida, tente novamente. ')
    print('-='*25)
print(f'Programa finalizado conforme solicitado! ')
