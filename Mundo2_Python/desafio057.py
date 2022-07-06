#código utilizando while para validação de resposta que aceita somente os valores 'M' e 'F'

s = ''
while s != 'M' and s != 'F':
    s = str(input('Gênero [M/F]: ')).upper().strip()[0]
    if s != 'M' and s != 'F':
        print(f'Dados inválidos. Tente novamente')
    else:
        print(f'Sexo {s} registrado com sucesso! Podemos prosseguir! ')
