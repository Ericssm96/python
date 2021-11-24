from time import sleep


def numeros(* valores):
    print('Os números foram ', end='')
    for i in range(0, len(valores)):
        print(valores[i], end=', ')
        sleep(0.3)
    print(f'No total foram digitados {len(valores)} números, e o maior deles foi o {max(valores)}')


numeros(1, 3, 4, 6, 7, 98, 34, 67)