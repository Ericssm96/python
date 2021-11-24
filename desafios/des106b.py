from time import sleep
c = ('\033[0;0m', '\033[1;93m', '\033[1;36m', '\033[;7m', '\033[1;35m', '\033[1;41m')


def ajuda(com):
    """
    -> apenas um help() com entrada em pt
    :param com: o que tiver na mensagem será mostrado no help
    :return: nada
    """
    titulo(f'Abrindo o manual do comando \'{com}\'.', cor=4)
    print(c[3], end='')
    help(com)
    print(c[0])


def titulo(msg='', cor=0):
    tam = len(msg)+2
    print(f'{c[cor]}', end='')
    if msg.strip() != '':
        print('~'*tam)
        print(f' {msg} ')
        print('~'*tam)
        sleep(0.5)


valor = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp.', 2)
    titulo(cor=1)
    valor = str(input('Digite a biblioteca ou função > '))
    print(c[0], end='')
    sleep(0.2)
    if valor.upper().strip() == 'FIM':
        break
    else:
        ajuda(valor)
titulo('Fim! Até mais!', cor=5)
