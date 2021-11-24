mat = [[], [], []], [[], [], []], [[], [], []]
somapar = somaterc = maiorseg = 0
for v in range(0, 3):
    for h in range(0, 3):
        n1 = int(input(f'Digite um valor para a casa [{v}][{h}]: '))
        mat[v][h].append(n1)
        if v == 1:
            if n1 > maiorseg:
                maiorseg = n1
        if h == 2:
            somaterc += n1
        if n1 % 2 == 0:
            somapar += n1
print(mat[0])
print(mat[1])
print(mat[2])
print('¨_'*8, end='')
print('Análise', end='')
print('¨_'*8)
print(f'A soma de todos os valores pares foi {somapar}.', end=' ')
print(f'A soma de todos os terceiros termos foi {somaterc}.', end=' ')
print(f'O maior número da segunda linha foi: {maiorseg}.')