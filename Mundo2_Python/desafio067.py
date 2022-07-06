tab = 0
while True:
    tab = int(input('Gostaria de ver a tabuada de qual número? '))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c:^2} = {c*tab:^2}')
print('~~'*30)
print('Programa tabuada finalizado. ')

