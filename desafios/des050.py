sp = 0
for c in range (1,7):
    num = int(input('Digite um número inteiro:\n'))
    if num % 2 == 0:
        sp = num + sp
print('A soma de todos os pares desse algorítmo é: {}.'.format(sp))
