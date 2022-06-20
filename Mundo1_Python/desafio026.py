frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece na frase ', frase.count('A'), ' vezes.')
print('A primeira vez que a letra A aparece é na posição: ', frase.find('A')+1)
print(f'A última vez que a letra A aparece é na posição: ', frase.rfind('A')+1)