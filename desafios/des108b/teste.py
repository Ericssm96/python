import moedarenom


n1 = float(input('Digite o preço: R$'))
print(f'O valor {moedarenom.moeda(n1)} dobrado é {moedarenom.moeda(moedarenom.dobro(n1))}.')
print(f'O valor {moedarenom.moeda(n1)} pela metade é {moedarenom.moeda(moedarenom.metade(n1))}.')
print(f'O valor {moedarenom.moeda(n1)} aumentado em 15% é {moedarenom.moeda(moedarenom.aumenta(n1, 15))}.')
print(f'O valor {moedarenom.moeda(n1)} diminuído em 15% é {moedarenom.moeda(moedarenom.diminui(n1, 15))}.')
