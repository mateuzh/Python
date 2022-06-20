'''Código que informa a hipotenusa com base no cateto oposto e cateto
adjacente utilizando math.'''


'''import math
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
h = co**2 + ca**2
h2 = math.sqrt(h)
print (f'Cateto oposto {co}² + cateto adjacente {ca}² = {h} ou {h2:.2f}²')'''

'''import math
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
h = (co**2 + ca**2) ** (1/2)
print (f'A hipotenusa vai medir {h:.2f}')'''

import math
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
hi = math.hypot(co,ca)
print (f'A hipotenusa vai ser {hi:.2f}')
