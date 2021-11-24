import datetime
ano = int(input('Digite um ano e eu te digo se ele é bissexto ou não, se zero for digitado, o ano considerado será o '
                'atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print('O ano {} é bissexto pois o resto da divisão dele por 4 é 0.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
print('fim')
