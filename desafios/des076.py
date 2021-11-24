lista = ('Arroz', 18.67, 'Feijão', 6.79, 'Batatas', 8.98, 'Computador', 3000.00, 'Celular', 1100.00, 'Teclado', 530,
         'Mouse', 400, 'Monitor', 800)
print('-'*20)
print('       LISTA       ')
print('-'*20)
print('-'*50)
for c in range (0, len(lista), 2):
    print(f'{lista[c]:.<30}R$', end=' ')
    print(f'{lista[c+1]:>7}')
print('-'*50)
