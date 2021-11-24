from random import choice
print('Vamos jogar Jo-ken-po!')
mj = choice(['pedra', 'papel', 'tesoura'])
sj = str(input('Pedra, papel ou tesoura?\n').lower())
if mj == 'pedra' and sj == 'tesoura':
    print('Eu jogo pedra, vc perdeu!')
elif mj == 'pedra' and sj == 'papel':
    print('Eu joguei pedra, vc ganhou!')
elif mj == 'papel' and sj == 'pedra':
    print('Eu joguei papel, vc perdeu!')
elif mj == 'papel' and sj == 'tesoura':
    print('Eu joguei papel, vc ganhou!')
elif mj == 'tesoura' and sj == 'papel':
    print('Eu joguei tesoura, vc perdeu!')
elif mj == 'tesoura' and sj == 'pedra':
    print('Eu joguei tesoura, vc ganhou!')
elif mj == sj:
    print('Eu joguei {} e você também, vamos começar de novo.'.format(mj))
else:
    print('Você não digitou um valor válido.')
