print('Bom dia!')
dist = float(input('Qual é a distância da sua destinação (em KM)? '))
if dist <= 200:
    pas = dist * 0.50
    print('O preço da passagem é {} reais.'.format(pas))
else:
    pas = dist * 0.45
    print('O preço fica {} reais.'.format(pas))
print('FIm')
