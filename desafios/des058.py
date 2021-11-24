import random
jia = random.randint(0, 10)
jm = 0
while jm != jia:
    jm = int(input('Digite um número de 0 a dez para ver se pensamos no mesmo número:\n'))
    if jm != jia:
        print('Ah, vc errou dessa vez, tente de novo.')
print('Acertou miseravi')
