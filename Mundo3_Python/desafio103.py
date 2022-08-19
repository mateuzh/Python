
def ficha(n=0, g=0):
    return f'O jogador {n if n != "" else "<não informado>"} fez {g if g != "" else "0"} gols'


nome = input('Nome do jogador: ')
gols = input('Quantos gols fez: ')
ficha(nome, gols)
print(ficha(nome, gols))
