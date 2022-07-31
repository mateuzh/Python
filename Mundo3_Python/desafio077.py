#Código para informar se há vogal na palavra que está em uma tupla

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for linhas in palavras:
    print(f'\nNa palavra {linhas} temos', end=' ')
    for vogais in linhas:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
