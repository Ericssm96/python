mat = [[], [], []], [[], [], []], [[], [], []]
for v in range(0, 3):
    for h in range(0, 3): #com essa estrutura posso ler os 9 valores da matriz, um em cada posição
        valor = (input(f'Digite o valor da posição {v}, {h}: '))
        mat[v][h].append(valor)
print(mat[0])
print(mat[1])
print(mat[2])
