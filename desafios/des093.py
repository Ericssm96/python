dados = {}
partidas = []
somagols = 0
dados['jogador'] = str(input('Digite o nome do jogador:\n'))
dados['quant'] = int(input('Em quantos jogos ele já esteve?\n'))
for k in range(0, dados['quant']):
    partidas.append(int(input(f'Quantos gols ele fez na partida {k+1}?\n')))
dados['totalgols'] = sum(partidas)
print(f'O total de gols foi {somagols} nas {dados["quant"]} partidas, sendo eles: ')
for i, c in enumerate(partidas):
    print(f'{c} gols na partida {i+1}.')
