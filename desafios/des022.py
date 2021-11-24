nome = str(input('Digite o seu nome completo: '))
esp = int(nome.count(' '))
car = int(len(nome))
let = car - esp
div = nome.split()
print('Seu nome com todas as letras maiúsculas fica {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas fica {}.'.format(nome.lower()))
print('A quantidade de letras apresentdas foi de {}.'.format(let))
print('A quantidade de letras no primeiro nome é: {}.'.format(len(div[0])))
