num = int(input('Digite um valor inteiro de 0 até 9999. '))
un = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}.'.format(num))
print('a unidade é {}.'.format(un))
print('a dezena é: {}.'.format(dez))
print('a centena é: {}.',format(cen))
print('o milhar é: {}.'.format(mil))
