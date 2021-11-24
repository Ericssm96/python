def resjogo(a, b=0):
    print(f'O jogador {a} fez {b} gol(s).')


j = input('Digite o nome do jogador: ')
g = input('Quantos gols ele fez? ')
if j == '':
    j = 'Misterioso'
if g.isnumeric():
    int(g)
else:
    g = 0
resjogo(j, g)
