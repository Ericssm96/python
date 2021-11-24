def notas(* aluno, sit=False):
    """
    :param aluno: Reune as notas dos alunos da classe
    :param sit: serve para mostrar se a média da classe ta aprovada ou reprovada
    :return: um dicionário com a maior nota, menor nota e a média, e o parâmetro opcional de situação.
    """
    maior = menor = soma = 0
    for i in range(0, len(aluno)):
        if i == 0:
            maior = aluno[i]
            menor = aluno[i]
        elif aluno[i] > maior:
            maior = aluno[i]
        elif aluno[i] < menor:
            menor = aluno[i]
        soma += aluno[i]
    bol = dict()
    bol['maiornota'] = maior
    bol['menornota'] = menor
    bol['media'] = soma/len(aluno)
    if sit:
        if bol['media'] >= 7:
            bol['situacao'] = 'Aprovados'
        else:
            bol['situacao'] = 'Reprovados'
    return bol


resp = notas(1, 3, 7, 8, 4, sit=True)
print(resp)
