import math
ang = int(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang)) #nesse caso o interpretador vai pegar o valor da variável ang, converter em radiano
# (que é o formato de número que a função math.sin() reconhece, e depois usar essa função para calcular o número desejado.
print('O ângulo de {} tem o seno com valor de: {:.2f}.'.format(ang, seno))
cosseno = math.cos(math.radians(ang)) #mesmo esquema
print('O ângulo de {} tem o seno com valor de : {:.2f}.'.format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('A tangente do ângulo {} é {}.'.format(ang, tangente))