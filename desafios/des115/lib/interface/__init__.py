def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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
    return int(n1)


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
    return float(n1)


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    print(lista)
    c = 1
    for item in lista:
        print(f'\033[1;92m{c} -\033[0;0m \033[1;95m{item}\033[0;0m')
        c += 1
    print(linha())
    opc = leiaint('\033[;7mDigite sua opção:\033[0;0m ')
    return opc
