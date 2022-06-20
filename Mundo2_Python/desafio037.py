#Código para conversão de números inteiros para BINÁRIO, OCTAL e HEXADECIMAL

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Para converter em BINÁRIO
[ 2 ] Para converter em OCTAL
[ 3 ] Para converter em HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} em BINÁRIO é igual a {num:b}!')
elif opção == 2:
    print(f'{num} em OCTAL é igual a {num:o}!')
elif opção == 3:
    print(f'{num} em HEXADECIMAL é igual a {num:x)}')
else:
    print('Opção inválida. Tente novamente.')