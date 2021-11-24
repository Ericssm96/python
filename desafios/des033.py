n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
n3 = input('Digite o último número: ')
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('A ordem do maior pro menor é: {}, {} e {}.'.format(n1, n2, n3))
    else:
        print('A ordem do maior pro meneor é: {}, {} e {}.'.format(n1, n3, n2))
else:
    if n2 > n1 > n3:
        print('')