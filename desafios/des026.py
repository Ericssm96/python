frase = input('Digite uma frase: ')
a = frase.upper().strip()
print('A letra "a" aparece {} vezes durante essa frase.'.format(a.count('A')))
print(a.find('A')+1)
print(a.rfind('A')+1)