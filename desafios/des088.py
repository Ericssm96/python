import random
print('#'*6, end='')
print('PALPITES DA LOTERIA', end='')
print('#'*6)
jogo = int(input('Quantos palpites de jogo você deseja fazer? '))
palpites = []
print('ANALISANDO...')
for i in range(0, jogo):
    for c in range(0, 6):
        n1 = random.randint(1, 60)
        palpites.append(n1)
        if palpites.count(n1) > 1:
            palpites.pop()
            c -= 1
    print(f'Jogo {i+1}: {palpites}.')
    palpites.clear()
print('Fim')