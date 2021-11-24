num = int(input('Digite um número inteiro para eu te dizer se ele é primo ou não:\n'))
p = 0
for c in range (1, num+1):
    if num % c == 0:
        p = p+1
if p == 2:
    print('é um número primo')
else:
    print('não é um número primo')
