import random
print('~'*30)
print('        Ímpar ou par.'    )
print('~'*30)
while True:
    jogpc = random.randint(1, 10)
    parimp = input('Você quer par (P) ou ímpar (I)?\n').strip().lower()
    if 'p' in parimp:
        minjog = int(input('Faça a sua jogada\n'))
        if (jogpc + minjog) % 2 == 0:
            print(f'A minha jogada foi: {jogpc}.')
            print('Parabéns, você ganhou')
        else:
            print(f'A minha jogada foi: {jogpc}')
            break
    elif 'i' in parimp:
        minjog = int(input('Faça a sua jogada\n'))
        if (jogpc + minjog) % 2 != 0:
            print('A minha jogada foi:'.format(jogpc))
            print('Parabéns, você ganhou!')
        else:
            print('A minha jogada foi: {}.'.format(jogpc))
            break
    else:
        print('Por favor, digite um valor válido.')
print('Você perdeu :(')