altc = float(input('Qual é a sua altura em centímetros? '))
peso = float(input('Qual é o seu peso? '))
altm = altc / 100
imc = peso / (altm * altm)
if imc < 18.5:
    print (f'Seu IMC foi de {imc:.2f} e você está \033[33m abaixo do peso! \033[m')
elif imc >= 18.5 and imc <= 25:
    print (f'Seu IMC foi de {imc:.2f} e você está no seu \033[32m peso ideal! \033[m')
elif imc > 25 and imc < 30:
    print (f'Seu IMC foi de {imc:.2f} e você está com \033[033m sobrepeso! \033[m ')
elif imc >= 30 and imc <= 40:
    print (f'Seu IMC foi de {imc:.2f} e você está com \033[35m obesidade! \033[m ')
elif imc > 40:
    print (f'Seu IMC foi de {imc:.2f} e você está com \033[31m obesidade morbida! \033[m')