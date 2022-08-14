def area(a, b):
    r = a * b
    print(f'A área do terreno com as medidas {a:.1f} e {b:.1f} é de {r:.1f}m²')



print(f' CÁLCULO DE TERRENOS!')
print(f'-'*40)
largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento (m): '))
area(largura, comprimento)