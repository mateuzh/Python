nota1 = float(input('Primeira nota: '))
nota2 = float (input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print (f'Sua média foi de \033[4m {media:.2f}\033[m, \033[1m e você está \033[31m REPROVADO \033[m!')
elif 7.0 > media >= 5.0:
    print (f'Sua média foi de \033[4m {media:.2f} \033[m, \033[1m e você está de \033[33m RECUPERAÇÃO \033[m!')
else:
    print (f'Sua média foi de \033[4m {media:.2f} \033[m! \033[1m Parabéns você está \033[34m APROVADO \033[m!')