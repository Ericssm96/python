import random

a1 = input('Escolha 1 dos alunos para ser sorteado: ')
a2 = input('Escolha outro: ')
a3 = input('Escolha mais um: ')
a4 = input('Escolha o último a ser um dos sorteados: ')
print('A ordem de apresentação será:{}'.format(random.sample([a1, a2, a3, a4], k=4))) #posso fazer assim, que é o jeito
#"mais simples", mas há outras maneiras.
#lista = (a1, a2, a3, a4).split()
#random.shuffle(lista)
#print(lista)
