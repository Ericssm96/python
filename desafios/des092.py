import datetime

dados = dict()
dados['nome'] = str(input('Digite o nome:\n'))
anonasc = int(input('Digite em que ano nasceu:\n'))
dados['idade'] = datetime.date.today().year - anonasc
dados['carteira'] = int(input('Digite o número da CTPS:\n'))
print(f'{dados}')
if dados['carteira'] != 0:
    dados['contrat'] = int(input('Em qual ano foi contratado?\n'))
    tempotrab = datetime.date.today().year - dados['contrat']
    dados['salario'] = float(input('E qual é o salário? '))
    dados['aposentadoria'] = dados['contrat'] + 40
    print(f'O nome do trabalhador em questão é {dados["nome"]}, de {dados["idade"]} anos. O mesmo foi possui a CLT sob '
          f'inscrição {dados["carteira"]} e foi contratado no ano {dados["contrat"]} pelo salário de R$ '
          f'{dados["salario"]}, portanto se aposentará quando tiver {dados["idade"]+(40-tempotrab)} anos.')
else:
    print(f'O nome é {dados["nome"]}, possui {dados["idade"]} anos e não possui nenhum reegistro de trabalho.')
