frase = input('Digite uma frase: \n').split()
primjoin = ''.join(frase) # essa é a estrutura
if primjoin[len(primjoin)::-1] == primjoin: #da minha palavra ao contrário
    print('Este é um palindroma válido, pois {} ao contrário é {}.'.format(primjoin[len(primjoin)::-1], primjoin))
else:
    print('Este conjunto de palavras não é um palíndromo válido.')
