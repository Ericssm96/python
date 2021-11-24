idgeral = 0
maisvel = 0
menos20 = 0
nomemaisvel = str
for c in range(1, 5):
    nome = input('Qual é o nome do personagem {}?\n'.format(c)).lower()
    idade = int(input('Qual é a idade?\n'))
    gen = input('Qual é o seu gênero?\n').lower()
    idgeral = idgeral + idade
    if 'masc' in gen or 'homem' in gen and idade > maisvel:
        maisvel = idade
        nomemaisvel = nome
    elif 'mulher' in gen or 'fem' in gen and idade < 20:
        menos20 = menos20 + 1
print('A média de idade é de {}'.format(idgeral/4))
print('O homem mais velho é {}, com {} anos.'.format(nomemaisvel, maisvel))
print('Tem um total de {} mulheres com menos de 20 anos aí.'.format(menos20))
