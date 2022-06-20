'''Código que diz quantos litros de tinta serão utilizados para pintar
determinada parede com variáveis definidas pelo usuário.'''

alt = float(input('Qual é a altura da parede? '))
larg = float (input ('Qual é a largura da parede? '))
area = larg * alt
qt = area / 2
print (f' A dimensão da sua parede é {larg} x {alt} e a quantidade de {area}m² \n Serão necessários {qt}l de tinta')