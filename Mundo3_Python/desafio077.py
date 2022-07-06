palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for linhas in palavras:
    print(f'Na palavra {linhas} temos', 'a' if 'A' in linhas else '',
          'e' if 'E' in linhas else '', 'i' if 'I' in linhas else '',
          'o' if 'O' in linhas else '', 'u' if 'U' in linhas else '')
