geral = [[], []]
for c in range(0, 7):
    n1 = int(input('Digite um valor: '))
    if n1 % 2 == 0:
        geral[0].append(n1)
    else:
        geral[1].append(n1)
geral[0].sort()
geral[1].sort()
print(f'Os valores pares ordenados foram: {geral[0]}.')
print(f'Os valores ímpares ordenados foram: {geral[1]}.')
