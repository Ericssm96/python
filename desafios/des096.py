def area(x, y):
    print('='*30)
    print(f'{"Tratando a área":^30}')
    print('='*30)

    a = x * y
    print(f'O valor da área de altura {x}m e largura {y}m é {a:.2f}m².')


area(float(input('Altura: ')), float(input('Largura: ')))