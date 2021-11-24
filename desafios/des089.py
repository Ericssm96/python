nome = []
notas = []
boletim = []
media = []
while True:
    namae = input('Digite o nome do/da aluno(a): ')
    nome.append(namae)
    n1 = float(input('Digite a nota da G1 dele/dela: '))
    notas.append(n1)
    n2 = float(input('Digite a nota da G2 dele/dela: '))
    notas.append(n2)
    nome.append(notas[:])
    boletim.append(nome[:])
    nome.clear()
    notas.clear()
    media.append((n1+n2)/2)
    conf = input('Deseja continuar (S/N)? ')
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = input('Digite uma alternativa válida: ')
print('ID', end='')
print(' '*18, end='')
print(f'Aluno', end='')
print(' '*10, end='')
print('Média')
print('='*42)
for i in range(0, len(boletim)):
    print(f'{i: <20}', end='')
    print(f'{boletim[i][0]: <15}', end='')
    print(f'{media[i]}')
print('='*42)
while True:
    perg = int(input('Deseja ver as notas do aluno de qual ID? (Digite 999 para sair)\n'))
    if perg == 999:
        break
    elif perg > len(boletim):
        perg = int(input(f'Valor inválido, digite novamente (só valores entre 0 e {len(boletim)}: '))
    print('='*70)
    print(f'O aluno do id {perg} é {boletim[perg][0]}, sua nota da G1 é {boletim[perg][1][0]}, e sua nota da G2 é '
          f'{boletim[perg][1][1]}.')
