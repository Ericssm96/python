import datetime
print('Olá, atleta!')
nasc = int(input('Em que ano você nasceu?'))
idade = datetime.date.today().year - nasc
if idade <= 9:
    print('Você é da categoria mirim!')
elif idade <= 14:
    print('Você é da categoria juvenil!')
elif idade <= 19:
    print('Você é da categoria junior!')
elif idade <= 20:
    print('Você é da categoria senior!')
else:
    print('Master')