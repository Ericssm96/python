import moedarenom


n1 = float(input('Digite o preço: R$'))
print(f'O valor {moedarenom.moeda(n1)} dobrado é {moedarenom.dobro(n1, True)}.')
print(f'O valor {moedarenom.moeda(n1)} pela metade é {moedarenom.metade(n1, True)}.')
print(f'O valor {moedarenom.moeda(n1)} aumentado em 15% é {moedarenom.aumenta(n1, 15, True)}.')
print(f'O valor {moedarenom.moeda(n1)} diminuído em 15% é {moedarenom.diminui(n1, 15, True)}.')
