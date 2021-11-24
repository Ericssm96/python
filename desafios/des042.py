n1 = int(input('Digite o valor de 1 dos lados do triângulo:\n'))
n2 = int(input('Digite o segundo valor:\n'))
n3 = int(input('Digite o terceiro valor:\n'))
if (n1 - n2) < n3 < n1 + n2 and (n1 - n3) < n2 < n1 + n3 and (n2 - n3) < n1 < n2 + n3:
    if n1 == n2 and n2 == n3:
        print('Estas medidas podem formar um triângulo equilátero.')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Estas medidas podem formar um triângulo isóceles.')
    elif n1 != n2 and n1!= n3:
        print('Estas medidas compõem um triângulo escaleno.')
else:
    print('Não dá pra montar um triângulo com essas medidas.')
