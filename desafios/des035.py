print('***************************')
print('*  Lados de um triângulo  *')
print('***************************')
print('Vamos testar com quais medidas pode ser composto um triângulo.')
l1 = float(input('Digite a medida de um dos lados do triângulo:\n'))
l2 = float(input('Digite a medida de outro lados do triângulo:\n'))
l3 = float(input('Digite a ultima medida para teste:\n'))
if (l2 - l3) < l1 < l2 + l3 and (l1 - l3) < l2 < l1 + l3 and (l2 - l1) < l3 < l2 + l1:
    print('Essas medidas podem formar um triângulo.')
else:
    print('Com essas aqui não dá, meu chapa.')
print('É isto')
