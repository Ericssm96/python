from random import randint
from time import sleep


def sorteio(lista):
    print('SORTEANDO')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.2)
    print('Fim!')


def mostrapar(itens):
    soma = 0
    print('Os valores pares são: ')
    for i in itens:
        if i % 2 == 0:
            soma += i
            print(i, end=' ')
    print(f'\nA soma desses valores foi {soma}.')


kah = []
sorteio(kah)
mostrapar(kah)
