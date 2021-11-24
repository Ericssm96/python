import random
a = random.randint(1, 9999)
b = random.randint(1, 9999)
c = random.randint(1, 9999)
d = random.randint(1, 9999)
e = random.randint(1, 9999)
meuvetor = (a, b, c, d, e)
print(f'Os termos foram: {meuvetor}.')
maior = sorted(meuvetor)[4] #ou eu posso simplesmente usar a função max(Tupla), que o Python já retorna o valor maximo
menor = sorted(meuvetor)[0] #mesma coisa com o min
print(f'O maior foi {maior}.')
print(f'O menor foi {menor}.')
