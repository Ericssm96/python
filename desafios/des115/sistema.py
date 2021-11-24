from des115.lib.interface import *
from des115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        cabecalho('Opção 1: ')
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2: ')
        nome = str(input('Digite o nome: '))
        idade = leiaint('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa...')
        break
    else:
        print('\033[1;31mErro! Digite um valor válido.\033[0;0m')
    sleep(1)
