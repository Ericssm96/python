import des109moeda


n1 = float(input('Digite o preço: R$'))
print(f'O valor {des109moeda.moeda(n1)} dobrado é {des109moeda.dobro(n1, True)}.')
print(f'O valor {des109moeda.moeda(n1)} pela metade é {des109moeda.metade(n1, True)}.')
print(f'O valor {des109moeda.moeda(n1)} aumentado em 15% é {des109moeda.aumenta(n1, 15, True)}.')
print(f'O valor {des109moeda.moeda(n1)} diminuído em 15% é {des109moeda.diminui(n1, 15, True)}.')
