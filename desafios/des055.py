mai = 0
men = 999999999999
for c in range(1,6):
    peso = float(input('Digite seu peso:\n'))
    if peso < men:
        men = peso
    elif peso > mai:
        mai = peso
print('O com maior peso pesava {}kg, enquanto o com menor peso pesava {}.'.format(mai, men))
