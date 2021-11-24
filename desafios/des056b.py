idgeral = 0
nomemaisvel = ''
idmaisvel = 0
men20 = 0
for c in range (1,5):
    print('----{}a pessoa----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').lower()
    idgeral = idade + idgeral
    if sexo == 'm' and idade > idmaisvel:
        idmaisvel = idade
        nomemaisvel = nome
    elif sexo == 'f' and idade < 20:
        men20 = men20 + 1
med = idgeral / c
print('A média de idade do grupo é de {} anos.'.format(med))
print('O homem mais velho tem {} anos e se chama {}.'.format(idmaisvel, nomemaisvel))
print('Ao todo são {} mulheres abaixo de 20 anos.'.format(men20))
