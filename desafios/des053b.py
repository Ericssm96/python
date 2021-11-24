frase = input('Digite uma frase para eu checar se é um palíndromo ou não:\n').lower().strip()
sep = frase.split()
junt = ''.join(frase)
inverso = ''
for c in range(len(junt)-1, -1, -1):
    inverso += junt[c]
print(inverso)
