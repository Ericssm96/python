aluno = dict()
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input('Digite a média dele: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
print(f'O aluno {aluno["nome"]} foi {aluno["situacao"]} pois sua média foi {aluno["media"]}.')