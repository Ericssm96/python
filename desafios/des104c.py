def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            valor = int(n1)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um valor inteiro.	\033[0;0m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'O número {n} é um número inteiro.')