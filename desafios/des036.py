print('******************')
print('*   EMPRÉSTIMO   *')
print('******************')
nome = input('Bom dia, senhor... Qual é o seu nome?\n')
sal = float(input('Bom dia, senhor {}, posso ver que o senhor precisa de um empréstimo para comprar uma casa, '
               'qual é o seu '
            'salário mensal?\n'.format(nome)))
valc = float(input('Qual é o valor da casa que o senhor deseja comprar?\n'))
ano = int(input('Em quanto tempo (em anos) o senhor pretende pagar esse empréstimo?\n'))
# calcule o valor da parcela MENSAL, sendo que a mesma não pode ser maior que 30% do salário do comprador,
# caso contrário o empréstimo é negado
mes = ano * 12
parc = valc / mes
if parc > (sal-sal*0.7):
    print('Erm, me desculpe, senhor {}, não foi possível aprovar o seu empréstimo nessas condições.'.format(nome))
else:
    print('Oba! Seu empréstimo foi aprovado!')
print('Muito obrigado pela preferência, {}.'.format(nome))
