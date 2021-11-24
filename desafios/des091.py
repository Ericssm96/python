from random import randint
from time import sleep
resultados = dict()
for i in range(0, 4):
    resultados[f'jogador{i+1}'] = randint(1, 6)
rank = sorted(resultados.values(), reverse=True)
for k, v in enumerate(rank):
    print(f'O jogador {k+1} tirou {v}.')
    sleep(1)