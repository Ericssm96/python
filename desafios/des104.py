def leiaint():
    a = input('Digite um número: ').strip()
    if not a.isnumeric():
        while not a.isnumeric():
            print(f'\033[1;31mERRO! DIGITE UM VALOR INTEIRO!')
            a = input('\033[0;0mDigite um número: ')
    print(f'Ok, o valor {a} é inteiro.')


leiaint()
