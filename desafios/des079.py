a = []
while True:
    n1 = int(input('Digite um número:\n'))
    a.append(n1)
    if a.count(n1) > 1:
        print('Esse valor não será adicionado, pois já foi uma vez.')
        a.pop()
    conf = input('Deseja continuar? (S/N)\n')
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = input('Por favor, digite uma alternativa válida (S/N):\n')
print(f'Os valores únicos digitados foram {sorted(a)}.')