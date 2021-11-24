pessoa = dict()
grupo = list()
maioridade = list()
idadetot = mul = 0
while True:
    pessoa['nome'] = str(input('Digite o nome do sujeito: '))
    while True:
        pessoa['sexo'] = str(input('Sexo (M/F)? ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite uma alternativa válida! (M/F)')
    if pessoa['sexo'] in 'F':
        mul += 1
    pessoa['idade'] = int(input('Quantos anos ele(a) tem? '))
    idadetot = idadetot + pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        conf = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
        if conf in 'SN':
            break
        else:
            print('ERRO! Por favor, digite uma alternativa válida (S/N).')
    if conf in 'N':
        break
print(grupo)
for i in grupo:
    if i['idade'] > idadetot / len(grupo):
        maioridade.append(i['nome'])
print(f'No total foram {len(grupo)} pessoas cadastradas, sendo {mul} dessas mulheres. A média de idade do grupo é '
      f'{idadetot/len(grupo):2f}, e os que são mais velhos que isso são: {maioridade}.')
