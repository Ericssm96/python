import random
n1 = float(input('Digite um valor:\n'))
n2 = float(input('Digite outro valor:\n'))
menu = 0
soma = 0
mult = 0
cont = 0
maior = 0
while menu != 5:
    cont += 1
    menu=int(input('''Digite o que deseja fazer com esse número:
    1)Somar
    2)Multiplicar
    3)Maior
    4)Novos números
    5)Sair do programa\n'''))
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}.'.format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('A múltiplicação entre {} e {} é: {}.'.format(n1, n2, mult))
    elif menu == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}.'.format(n2, n1))
        elif n1 == n2:
            print('Ambos os valores são iguais.')
    elif menu == 4:
        n1 = int(input('Digite o novo valor para ooo primeiro número:\n'))
        n2 = int(input('Digite o novo valor para o segundo número:\n'))
print('Fim')
