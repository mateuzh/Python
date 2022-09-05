#código de tabuada utilizando laço de repetição for

escolha = int(input('Gostaria de saber a tabuada de qual número? '))
print(f'Tabuada do: ', escolha)
for c in range(1, 11):
    print(escolha,' x ', c, ': ', c * escolha )