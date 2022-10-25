import moeda

preço = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(preço)} é: {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é: {moeda.dobro(preço, True)}')
print(f'Aumentando {moeda.moeda(preço)} em 10%: {moeda.aumentar(preço, True)}')
print(f'Diminuindo {moeda.moeda(preço)} em 13%: {moeda.diminuir(preço, True)}')
