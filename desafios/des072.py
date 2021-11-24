extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n1 = int(input('Digite um número para ser escrito por extenso.\n'))
    while n1 < 0 or n1 > 20:
        n1 = int(input('Por favor, digite um valor válido:\n'))
    print(extenso[n1])
    conf = input('Deseja tentar novamente? (S/N)')
    if conf in 'Nn':
        break
print('Fim')