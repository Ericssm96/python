a = []
c = 0
while True:
    a.append(int(input('Digite um número:\n')))
    c += 1
    conf = input('Deseja digitar mais um? (S/N)\n').strip().lower()
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = input('Digite uma alternativa válida.\n')
print(f'Foram digitados {c} números.')
if 5 in a:
    print(f'O número 5 apareceu {a.count(5)} vez(es).')
else:
    print('O número 5 não apareceu entre esses números.')
a.sort(reverse=True)
print(a)
