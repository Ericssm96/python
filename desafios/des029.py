from random import randint
vel = randint(0,300)
multa = (vel - 80)*7
if vel > 80:
    print('Você estava andando acima do limite de 80 km! Sua velocidade era {} e o valor da multa que tem que pagar é de {} dólares.'.format(vel, multa))
else:
    print('Muito bem, meu bom senhor, pode ir andando.')
print('Câmbio, desligo.')
