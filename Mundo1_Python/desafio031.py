#Cálculo do valor da passagem.
from time import sleep
distancia = float(input('Qual será a distância da sua viagem? '))
print ('Calculando o valor da sua passagem...')
sleep(1)
print (f'O valor da sua passagem será {distancia*0.50}' if distancia <=200 else f'O valor da sua passagem será {distancia*0.45}')


