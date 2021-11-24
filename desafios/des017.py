import math
catop = float(input('Qual é o valor do cateto oposto do triângulo? '))
catad = float(input('Digite o valor do cateto adjacente do triângulo: '))
hip2 = (catop ** 2) + (catad ** 2)
hip = math.sqrt(hip2)
print('O comprimento da sua hipotenusa, somando o {}²+{}² foi {}, e tirando a raiz quadrada desse valor, temos {}, que é o valor da hipotenusa.'.format(catop, catad, hip2, hip))
