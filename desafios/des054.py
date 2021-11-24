import datetime
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite em que ano você nasceu:\n'))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('São {} maior(es) de idade e {} menor(es) de idade.'.format(maior, menor))
