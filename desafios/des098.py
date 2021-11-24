from time import sleep


def contagem(ini, fim, passo):
    print('%'*30)
    if fim > ini:
        while ini <= fim :
            print(ini, end=' ')
            if passo == 0:
                passo += 1
            ini += passo
            sleep(0.3)
        print('Fim!')
        sleep(0.2)
    else:
        while fim <= ini:
            print(ini, end=' ')
            if passo < 0:
                ini += passo
            elif passo == 0:
                passo += 1
                ini -= passo
            else:
                ini -= passo
            sleep(0.3)
        print('Fim!')
        sleep(0.2)


contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora você faz os termos da contagem!')
sleep(0.2)
contagem(int(input('Quantia inicial: ')), int(input('Quantia final: ')), int(input('Passo: ')))