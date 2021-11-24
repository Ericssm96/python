n1 = int(input('Digite um número para calcular o fatorial dele:\n'))
c = n1
mult = 1
while c > 0:
    print('{}'.format(c), end='')
    mult = mult * c
    c -= 1
    print('x' if c >= 1 else '=', end='')
print(mult)
