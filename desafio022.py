nome = str(input('Digite seu nome completo: ')).strip()
print (f'Seu nome inteiro em letra maiúscula: {nome.upper()}')
print (f'Seu nome inteiro em letra minúscula: {nome.lower()}')
nome1 = nome.split()
nomesemespaco = ''.join(nome1)
print(f'Seu nome tem ao todo {len(nomesemespaco)} caracteres')
print(f'Seu primeiro nome é {nome1[0]} e ele tem {len(nome1[0])} letras.')





