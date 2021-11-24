def leiaint(a):
    n = str(input(a))
    while not n.isnumeric():
        print('\033[1;31mERRO! Digite um valor válido!\033[0;0m')
        n = str(input(a))
    if n.isnumeric():
        int(n)
        print(f'Ok, o número {n} é inteiro.')


leiaint('Digite um número: ')
