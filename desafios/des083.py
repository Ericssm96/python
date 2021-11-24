exp = str(input('Digite uma expressão matemática:\n'))
parent = []
for simb in exp:
    if simb == '(':
        parent.append('(')
    if simb == ')':
        parent.pop()
if len(parent) != 0:
    print('Sua expressão é inválida.')
else:
    print('Sua expressão é válida.')
