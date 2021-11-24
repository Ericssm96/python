print('Vou converter um número que você digitar em binário, octal e hexadecimal.')
num = int(input('Digite um número: '))
alt = int(input('''Digite uma alternativa para conversão, sendo ela
            [1] para binário
            [2] para octal
            [3] para hexadecimal.'''))
if alt == 1:
    print('O numero {} convertido em binário é {}.'.format(num, bin(num)[2:]))
elif alt == 2:
    print('O número {} convertido em octal é {}.'.format(num, oct(num)[2:]))
elif alt == 3:
    print('O número {} convertido em hexadecimal é {}.'.format(num, hex(num)[2:]))
