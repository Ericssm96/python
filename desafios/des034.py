sal = float(input('Digite seu salário atual:\n'))
if sal >= 1200:
    aum = sal + (sal*0.15)
    print('Seu salário vai de R${} para R${}.'.format(sal, aum))
else:
    aum = sal + (sal*0.2)
    print('Seu salário vai de R${} para R${}.'.format(sal, aum))
print('Agora vai lá comemorar comendo umas puta')
