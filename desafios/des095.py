geral = []
jogador = {}
gols = []
total = 0
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['quant'] = int(input(f'Quantas partidas {jogador["nome"]} jogou nesse campeonato? '))
    for i in range(0, jogador['quant']):
        gols.append(int(input(f'Quantos gols ele fez na partida {i+1}? ')))
        total = total + gols[i]
    jogador['partida'] = gols[:]
    jogador['total'] = total
    geral.append(jogador.copy())
    jogador.clear()
    gols.clear()
    total = 0
    i = 0
    conf = str(input('Deseja continuar (S/N)? '))
    if conf in 'Ss' or conf in 'Nn':
        if conf in 'Nn':
            break
    else:
        conf = str(input('Por favor, digite uma opção válida (S/N): '))
print(f'|{"id": <3}||{"nome": <17}||{"gols": <19}||{"TOTAL"}|')
for i in range(0, len(geral)):
    print(f'|{i+1:<3}||{geral[i]["nome"]:<17}||{str(geral[i]["partida"]):<19}||{geral[i]["total"]:<5}|')
while True:
    perg = int(input('Deseja mostrar o aproveitamento detalhado de qual jogador (id)? '))
    if perg == 999:
        break
    while perg > len(geral):
        perg = int(input(f'Por favor, digite um valor válido (entre 1 e {len(geral)}: '))
    print(f'O jogador {perg} é {geral[perg-1]["nome"]}.')
    for k, v in enumerate(geral[perg-1]['partida']):
        print(f'Na partida {k+1} fez {v} gols.')
