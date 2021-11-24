n1 = int(input('Digite o primeiro termo de uma PA.'))
raz = int(input('Digite a razão dessa PA.'))
c = 1
termo = n1
mais = 1
total = 10
while mais != 0:
    while c <= total:
        print(termo+raz)
        c += 1
        termo = termo + raz
    mais = int(input('Deseja mostrar mais quantos termos?'))
    total = total + mais
print('FIM PORRAAAAAAAAAAAAAAAAAAAA')
