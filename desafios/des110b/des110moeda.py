def aumenta(n, porc=0, form=False):
    realporc = porc/100
    pf = n + (n*realporc)
    if form:
        f = f'R${pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def dobro(n, form=False):
    pf = n * 2
    if form:
        f = f'R${pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def metade(n, form=False):
    pf = n / 2
    if form:
        f = f'R${pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def diminui(n=0, porc=0, form=False):
    pf = n - n*(porc/100)
    if form:
        f = f'R${pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def moeda(n, md='R$'):
    return f'{md}{n:.2f}'.replace('.', ',')


def resumo(n, aum=0, dim=0):
    print('-'*30)
    print('Resumo do preço'.center(30))
    print('-'*30)
    print(f'{"Preço analisado:"}\t\t{moeda(n)}')
    #print(f'{"Dobro do preço:":<25}{dobro(n, True)}')
    print(f'{"Dobro do preço:"}\t\t\t{dobro(n, True)}')
    #print(f'{"Metade do preço:":<25}{metade(n, True)}')
    print(f'{"Metade do preço:"}\t\t{metade(n, True)}')
    #print(f'{f"Preço aumentado em {aum}%:":<25}{aumenta(n, aum, True)}')
    #print(f'{f"Preço diminuído em {dim}%:":<25}{diminui(n, dim, True)}')
    print(f'{f"Preço aumentado em {aum}%:"}\t{aumenta(n, aum, True)}')
    print(f'{f"Preço aumentado em {dim}%:"}\t{diminui(n, dim, True)}')
    print('-'*30)
