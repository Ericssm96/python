n1 = int(input('Digite um número como base para a PA:\n'))
raz = int(input('Digite a razão\n'))
c = 1
while c < 11:
    print(n1+c*raz)
    c += 1
conf = int(input('Quantos termos mais deseja digitar?'))
c1 = c + conf #contador para parâmetro de multiplicação com a razão na continuação.
c2 = c1
#if conf != 0:  esse funcionou mas não como eu queria então vamo deixar a ideia congelada aqui
while conf != 0:
    while c < c2:
        print(n1+(raz*c1))
        c += 1
        c1 += 1
    conf = int(input('Deseja exibir mais quantos termos?'))
    c = c-c3
    c3 = 0
    c1 = c1 - c3
    c2 = conf +
print('Fim')