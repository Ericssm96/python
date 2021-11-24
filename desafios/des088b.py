from random import randint
palpite = []
jog = []
jogcop = []
qtd = int(input('Digite quantos jogos você quer fazer: '))
i = 0
c = 0
while i < qtd:
    while c < 6:
        n1 = randint(1, 60)
        if n1 not in jog:
            jog.append(n1)
            c += 1
    jog.sort()
    palpite.append(jog[:])
    jog.clear()
    c = 0
    print(f'{i+1}° jogo: {palpite[i]}.')
    i += 1
