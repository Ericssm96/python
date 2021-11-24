from time import sleep


def maior(* lista):
    maior = 0
    for c in lista:
        if c > maior:
            maior = c
    print(maior)


maior(2, 4, 5, 9, 5, 4,1)