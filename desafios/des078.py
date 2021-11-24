a = []
mai = men = 0
for c in range(0, 5):
    a.append(int(input('Digite um número para a lista:\n')))
    if c == 0:
        mai = a[c]
        men = a[c]
    if a[c] > mai:
        mai = a[c]
    if a[c] < men:
        men = a[c]
print(a)
print(f'O maior valor é {mai}, na(s) posição(ções): ', end='')
for i, v in enumerate(a):
    if v == mai:
        print(f'{i+1}',end='... ')
print(f'O menor valor é {men}, na(s) posição(ções): ', end='')
for i, v in enumerate(a):
    if v == men:
        print(f'{i+1}', end='... ')
