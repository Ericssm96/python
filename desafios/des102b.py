def fat(a=3, show=False):
    if show:
        f = 1
        for c in range(a, 0, -1):
            f *= c
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        return f
    else:
        f = 1
        for c in range(a, 0, -1):
            f *= c
        return f


n1 = int(input('What number do you wish to see the factorial value of? '))
conf = bool(input('Type anything if you wanna see the formula (if you do not, just press ENTER). '))
resp = fat(n1, conf)
print(resp)
