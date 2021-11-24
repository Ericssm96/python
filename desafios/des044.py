preco = float(input('Digite o preço do programa:\n'))
mp = input('Qual vai ser o método de pagamento?\n').lower().strip()
if 'cartão' in mp:
    parc = int(input('Em quantas parcelas você deseja pagar o programa? (sendo 1 ou 0 considerada à vista)'))
    if parc < 2:
        desc = preco * 0.05
        print('Com o seu desconto de {} reais, o preço final ficou {}.'.format(desc, preco - desc))
    elif parc == 2:
        print('O valor a ser pago será: {}.'.format(preco))
    elif parc < 2:
        desc = preco * 0.2
        print('O valor a ser pago será: {}!'.format(preco + desc))
elif 'dinheiro' in mp or 'cheque' in mp:
    desc = preco * 0.1
    print('A quantia a ser paga será: {}!!!!'.format(preco - desc))
else:
    print('Valor inválido')
    