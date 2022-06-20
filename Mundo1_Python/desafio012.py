'''Código que calcula o desconto a ser dado para determinado preço
com porcentagem de desconto definida em 5%.'''

preco = float(input('Digite o preço do produto: R$'))
desc = preco * (5/100)
print (f' Com a promoção de 5% você terá R${desc} de desconto! \n O valor do produto ficará em R${preco-desc}.')