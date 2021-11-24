def aumenta(n, porc=0, form=False):
    realporc = porc/100
    pf = n + (n*realporc)
    if form:
        f = f'{pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def dobro(n, form=False):
    pf = n * 2
    if form:
        f = f'{pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def metade(n, form=False):
    pf = n / 2
    if form:
        f = f'{pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def diminui(n=0, porc=0, form=False):
    pf = n - n*(porc/100)
    if form:
        f = f'{pf:.2f}'.replace('.', ',')
        return f
    else:
        return pf


def moeda(n, md='R$'):
    return f'{md}{n:.2f}'.replace('.', ',')


def resumo(n, aum=0, dim=0):
    valaum = n + (n*(aum/100))
    valdim = n - (n*(aum/100))
    valdob = n * 2
    valmet = n / 2
    f = str(n).replace('.', ',')+'0'
    print('-'*30)
    print(f'{"Resumo do preço":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<25}{f}')
    print(f'{"Dobro do preço:":<25}{str(valdob).replace(".", ",")}0.')
    print(f'{"Metade do preço:":<25}{str(valmet).replace(".", ",")}0.')
    print(f'{f"Preço aumentado em {aum}%:":<25}{str(valaum).replace(".", ",")}0.')
    print(f'{f"Preço diminuído em {dim}%:":<25}{str(valdim).replace(".", ",")}0.')
    print('-'*30)
