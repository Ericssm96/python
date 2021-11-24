print('Vamos calcular seu IMC!')
alt = str(input('Digite sua altura:\n')).replace(',', '.').strip()
alt = float(alt)
peso = str(input('Digite o seu peso:\n')).replace(',', '.').strip()
peso = float(peso)
imc = peso / (alt**2)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Obesidade mórbida amigo pode cuidar.')
