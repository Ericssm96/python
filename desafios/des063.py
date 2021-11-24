print('=-=-=-=-=-=-=-=-=-=')
print('        Fibo      ')
print('=-=-=-=-=-=-=-=-=-=')
final = int(input('Quantos termos da sequência de Fibonacci você quer exibir?'))
t1 = 0
t2 = 1
t3 = 0
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= final:
    print(' -> {}'.format(t3), end='')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
print('-> Fim.')
