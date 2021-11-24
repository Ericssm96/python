print('Olá')
n1 = 0
soma = 0
c = 0
while n1 != 999:
    n1 = int(input('Digite um número qualquer:\n'))
    if n1 != 999:
        soma = soma + n1
    c += 1
print('{} números foram digitados.'.format(c))
print('A soma desses números foi: {}.'.format(soma))
print('Fim')
