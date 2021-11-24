def leiadinheiro(txt):
    from utilidadescev import moeda
    valor = 0
    ok = False
    while True:
        n1 = input(txt).replace(',', '.').strip()
        if n1.replace('.', '').isnumeric():
            ok = True
        else:
            print(f'\033[1;31mERRO! "{n1}" é um valor inválido. Por favor, digite um valor válido.\033[0;0m')
        if ok:
            break
    return float(n1)
