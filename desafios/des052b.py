num = int(input('Digite um número:\n'))
div = 0
for c in range (1, num+1):
    if num % c == 0:
        print('\33[33m', end='')
        print('{}'.format(c), end='. ')
        div = div + 1
    else:
        print('\33[31m', end='')
        print('{}'.format(c), end='. ')
if div > 2:
    print('\33[13m')
    print('Este não é um número primo.')
else:
    print('\33[13m')
    print('Este é um número primo.')