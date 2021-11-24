hom = men18 = mulmen20 = 0
while True:
    print('---CADASTRO---')
    idade = int(input('IDADE: '))
    if idade < 18:
        men18 += 1
    sexo = input('SEXO (F/M): ').strip().lower()
    while sexo not in 'FfMm':
        sexo = input('SEXO (F/M): ').strip().lower()
    if sexo in 'Ff' and idade < 20:
        mulmen20 += 1
    if sexo in 'Mm':
        hom += 1
    conf = input('CONTINUAR? (S/N) ').strip().lower()
    while conf not in 'SsNn':
        conf = input('CONTINUAR? (S/N) ').strip().lower()
    if conf in 'Nn':
        break
print(f'A quantidade de pessoas menores de idade é: {men18}.')
print(f'A quantidade de homens cadastrados foi {hom}.')
print(f'A quantidade de mulheres menores que 20 anos foi {mulmen20}.')
print('-------Fim-------')
