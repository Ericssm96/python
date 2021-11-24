palavras = ('Karate', 'Dinamite', 'Curso', 'Aprender', 'Perfil', 'Veloz', 'Andar', 'Apontar', 'Saber', 'Ligar')
for c in range(len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos: ', end='')
    for c2 in range(len(palavras[c])):
        if palavras[c][c2] in 'Aa' or palavras[c][c2] in 'Ee' or palavras[c][c2] in 'Ii' or palavras[c][c2] in 'Oo' \
                or palavras[c][c2] in 'Uu':
            print(palavras[c][c2], end=' ')
