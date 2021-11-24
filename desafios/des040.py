n1 = float(input('Qual foi a primeira nota do aluno?\n'))
n2 = float(input('E a segunda nota?\n'))
media = n1 + n2 / 2
if media < 5:
    print('fracassado')
elif 5 <= media <=6.9:
    print('recuperação')
else:
    print('passou')