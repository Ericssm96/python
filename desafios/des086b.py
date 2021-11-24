mat = [[], [], [], [], [], [], [], [], []]
for v in range(0, 3):
    for h in range(0, 3):
        n1 = int(input(f'Digite o valor da casa [{v}][{h}]'))
        mat[v][h].append(n1);

print(mat)