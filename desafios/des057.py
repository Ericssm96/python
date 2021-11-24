sexo = input('Digite o seu sexo (F/M):').lower()
while sexo != 'f' and sexo != 'm':
    sexo = input('Por favor, digite um valor coreto (F ou M).\n').lower()
print('Obrigado')
# ou while sexo not in 'FfMm':