mu = c = 1
while True:
    n1 = int(input('Você quer fazer a tabuada de qual número?\n'))
    if n1 < 0:
        break
    while c <=10:
        mu = n1 * c
        print(f'{n1} x {c} = {mu}')
        c += 1
    c = 0
print('Fim')