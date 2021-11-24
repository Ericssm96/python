pessoas = []
qtd = maiorp = menorp = 0
nomesgordos = nomesmagros = []
while True:
    nome = str(input('Digite um nome:\n'))
    pessoas.append(nome)
    peso = int(input('Digite o peso:\n'))
    pessoas.append(peso)
    if qtd == 0:
        maiorp = peso
        menorp = peso
    elif peso > maiorp:
        maiorp = peso
    elif peso < menorp:
        menorp = peso
    conf = str(input('Deseja continuar (S/N)?\n'))
    qtd += 1
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = str(input('Digite um valor válido:\n'))
print(f'Foram cadastradas {qtd} pessoas, sendo elas: {pessoas}.')
for p in range(1, len(pessoas)+1, 2):
    if pessoas[p] >= maiorp:
        nomesgordos.append(pessoas[p-1])
    elif pessoas[p] <= menorp:
        nomesmagros.append(pessoas[p-1])
if len(nomesmagros) == 1:
    print(f'A pessoa mais magra que tem é {nomesmagros}.')
elif len(nomesmagros) > 2:
    print(f'As pessoas mais magras são: {nomesmagros}.')
if len(nomesgordos) == 1:
    print(f'A pessoa mais gorda que tem é {nomesgordos}.')
elif len(nomesgordos) > 1:
    print(f'As pessoas mais gordas que têm são: {nomesgordos}.')