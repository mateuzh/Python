#dicionários identificados por {}, dict{} ou somente {}

filmes = {'título': 'Star Wars',
          'ano': '1989',
          'diretor': 'George Lucas'}
print(f'O filme {filmes["título"]} é dirigido por {filmes["diretor"]} e foi lançado no ano {filmes["ano"]}')
for k, v in filmes.items():
    print(f'O {k} é {v}')