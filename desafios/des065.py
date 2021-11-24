c = 0
mai = 0
men = 0
conf = 'sim'
soma = 0
while 's' in conf:
    n1 = int(input('Digite  um número: '))
    soma = n1 + soma
    if c == 0:
        men = n1
        mai = n1
    elif n1 > mai:
        mai = n1
    elif n1 < men:
        men = n1
    conf = input('Você deseja ir de novo? [S/N]').lower()
    c += 1
print('A média entre esss números é de {}.'.format(soma/c))
print('O maior entre esses números foi o {} e o menor foi {}.'.format(mai, men))
print('Fim')