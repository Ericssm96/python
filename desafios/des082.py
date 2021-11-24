a = []
par = []
impar = []
while True:
    a.append(int(input('Digite um número:\n')))
    conf = input('Deseja continuar? (S/N)\n')
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = input('Digite um valor válido:\n')
for i in a:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'A primeira lista foi: {a}.')
print(f'A lista com os valores pares dela ficou dessa maneira: {par}.')
print(f'A lista com os valores ímpares dela ficou dessa maneira: {impar}.')
