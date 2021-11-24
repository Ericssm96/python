from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogadores.items():
    print(f'{k} tirou {v}.')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)#esse itemgetter serve para fazer com que o
# parâmetro para organização do sorted seja o item na posição 1, que no caso seria o randint(1, 6). se o proograma
# fosse feito apenas com o jogadores.values() e o reverse, o maior valor de jogada sempre seria mostrado como jogador 1.
for i, c in enumerate(ranking):
    print(f'O {ranking[i][0]} tirou {ranking[i][1]}, e com isso ficou em {i+1}° lugar.')
    sleep(1)
