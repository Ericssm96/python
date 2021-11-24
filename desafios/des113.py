def leiaint(a):
    while True:
        n1 = input(a)
        try:
            int(n1)
        except ValueError:
            if n1 != '':
                print('\033[1;31mErro! Digite um valor inteiro, por favor.\033[0;0m')
            else:
                n1 = 0
                print('\033[;7mNo caso de ausência de digitação, o número recebe 0.\033[0;0m')
                break
        else:
            break
    return n1


def leiafloat(b):
    while True:
        n1 = input(b)
        try:
            float(n1)
        except ValueError:
            if n1 != '':
                print('\033[1;31mErro! Só números reais.\033[0;0m')
            else:
                print('\033[;7mNo caso de ausência de digitação a variável recebe 0.\033[0;0m')
                n1 = float(0)
                break
        else:
            break
    return n1


n2 = leiaint('Digite um número inteiro: ')
n3 = leiafloat('Digite um número real: ')
print(f'O número {n2} é inteiro, enquanto o {n3} é real.')