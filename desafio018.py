'''Código que informa o SENO, COSSENO E TANGENTE com base no
ângulo digitado utilizando math.'''

from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
print (f'O ângulo de {a} tem o SENO de {s:.2f}')
c = cos(radians(a))
print (f'O ângulo de {a} tem o COSSENO de {c:.2f}')
t = tan(radians(a))
print (f'O ângulo de {a} tem a TANGENTE de {t:.2f}')