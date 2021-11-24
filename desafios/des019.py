import random
a1 = input('Escolha 1 aluno pra ser um dos possíveis sorteados do professor. ')
a2 = input('Escolha outro aluno para ser um dos possíveis escolhidos. ')
a3 = input('Escolha outro aluno para poder ser escolhido. ')
a4 = input('Escolha o último aluno: ')
print('O professor vai escolher {} para apagar o quadro.'.format(random.choice([a1, a2, a3, a4])))
