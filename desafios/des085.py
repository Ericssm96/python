par = []
impar = []
geral = []
for i in range(0,7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        par.append(n1)
    else:
        impar.append(n1)
impar.sort()
par.sort()
geral.append(par)
geral.append(impar)
print(f'Os números foram: {geral}, sendo os pares {par} e os ímpares {impar}.')
print('='*15, end='')
print('Fim', end='')
print('='*15)
