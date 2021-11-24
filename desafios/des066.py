c = soma = 0
while True:
    n1 = int(input('Digite um número:\n'))
    if n1 == 999:
        break
    soma += n1
    c += 1
print(f'Você digitou {c} números. A soma deles é {soma}')