mintupla = (int(input('Digite um número:\n')), int(input('Digite outro número:\n')), int(input('Digite mais um '
                                                                                               'número')),
            int(input('Digite o último número:\n')))
if 3 in mintupla:
    pos3 = mintupla.index(3)+1
else:
    pos3 = 0
qnt9 = mintupla.count(9)
print(f'Os números digitados foram: {mintupla}.')
print(f'{qnt9} desses números foi/foram o número 9.')
if pos3 != 0:
    print(f'A posição do primeiro 3 foi: {pos3}')
else:
    print('O número 3 não apareceu nenhuma vez entre os números.')
print(f'Os numeros pares que apareceram foram:',end=' ')
for cont in range(0,len(mintupla)):
    if mintupla[cont] % 2 == 0:
        if cont < len(mintupla):
            print(mintupla[cont], end='')
