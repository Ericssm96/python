a = []
for c in range(0, 5):
    n1 = int(input('Digite um número:\n'))
    if c == 0 or n1 > a[len(a)-1]:
        print(f'O número {n1} foi inserido no final.')
        a.append(n1)
    else:
        pos = 0
        while pos < len(a):
            if n1 <= a[pos]:
                print(f'O número {n1} foi inserido na posição {pos+1}.')
                a.insert(pos, n1)
                break
            pos +=  1
print(a)
