def fat(a=7, show=False):
    """
    :param a: is the value the user wants to see the factorial of
    :param show: checks if it should show the formula behind the calculation
    :return: the factorial value of the number
    """
    f = 1
    for c in range(a, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


n1 = int(input('What number do you wish to see the factorial value of? '))
conf = bool(input('Type anything if you want to see the formule behind it.'))
fat(n1, conf)
