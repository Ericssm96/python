import random
ran = random.randint(0,5)
palp = int(input('Tente adivinhar com um palpite se você consegue adivinhar no número entre 0 e 5 que eu pensei: '))
if palp == ran:
    print('Parabéns, você é ninja!')
else:
    print('Não se preocupe, há sempre outra chance')
print('Fim.')
