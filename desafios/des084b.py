pessoa = []
grupo = []
magros = []
gordos = []
maiorp = menorp = c = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if c == 0:
        maiorp = pessoa[1]
        menorp = pessoa[1]
    elif pessoa[1] > maiorp:
        maiorp = pessoa[1]
    elif pessoa[1] < menorp:
        menorp = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    c += 1
    conf = str(input('Deseja continuar? '))
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = str(input('Por favor, digite uma alternativa válida (S/N): '))
print(grupo)
for pessoa in grupo:
    if pessoa[1] == maiorp:
        gordos.append(pessoa[0])
    elif pessoa[1] == menorp:
        magros.append(pessoa[0])
print(f'O maior peso foi {maiorp} e a(s) pessoa(s) que o possui/possuem é/são: {gordos}.')
print(f'O menor peso foi {menorp} e a(s) pessoa(s) que o possui/possuem é/são: {magros}.')
