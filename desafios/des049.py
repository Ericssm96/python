num = int(input('Digite um número para saber a tabuada dele.\n'))
for c in range (1,11):
    print ('{} x {} = {}'.format(num, c, num * c))
print('Fim')