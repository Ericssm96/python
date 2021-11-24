print('~'*30)
print('BANCOS AVORIK')
print('~'*30)
nt50 = nt20 = nt10 = nt1 = 0
saque = int(input('Quantos R$ deseja sacar?\n'))
resto = saque
while True:
    if resto > 50:
        nt50 = resto // 50
        resto = resto  % 50
        print(f'{nt50} nota(s) de R$ 50.')
    if resto > 20:
        nt20 = resto // 20
        resto = resto % 20
        print(f'{nt20} nota(s) de R$ 20.')
    if resto > 10:
        nt10 = resto // 10
        resto = resto % 10
        print(f'{nt10} nota(s) de R$ 10.')
    if resto > 1:
        nt1 = resto // 1
        resto = resto % 1
        print(f'{nt1} nota(s) de R$ 1.')
    if resto == 0:
        break
print('Fim')