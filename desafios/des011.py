altpar = float(input('Qual é a altura (em metros) da parede atrás de você? '))
largpar = float(input('E qual é a largura? '))
areapar = altpar * largpar
tinta = areapar/2
print('A área da sua parede é {} e serão necessários {} litros de tinta para colorir ela por inteiro.'.format(areapar, tinta))
