mai = 0
men = 0
for i in range (1,6):
    peso = float(input('Digite o peso da {}a pessoa.'.format(i)))
    if i == 1:
        men = peso
        mai = peso
    elif peso < men:
        men = peso
    elif peso > mai:
        mai = peso
print('O com maior peso foi {} e o com menor foi {}.'.format(mai, men))
