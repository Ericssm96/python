#import random
import math

#n = random.uniform(1.0, 1000.00) eu entendi que era pra pegar numero aleatório mas fodase pelo menos aprendi
#print('Seu número foi {:.3f}, e a parte inteira dele é {}.'.format(n, math.floor(n)))
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n,math.floor(n))) #também pode ser usado o math.trunc(), ou
# apenas converter em int usando "int(n)"
