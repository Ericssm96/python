def ajuda():
    while True:
        print('\033[1;36m~'*32)
        print(f'{"Sistema de ajuda PyHelp":^32}')
        print('~'*32, end='\033[0;0m\n')
        print(help(input('\033[1;42mDigite qual comando deseja ver?\033[0;0m ')))

        conf = input('Deseja continuar (S/N)? ').strip().upper()
        if conf in 'N':
            break


ajuda()
