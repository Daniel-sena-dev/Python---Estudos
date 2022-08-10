def validacao(msg):
    valido = False

    while not valido:
        numero = str(input(msg)).strip()

        if numero.isalpha() or numero == '':
            print(f'ERRO: \"{numero}\" é um preço inválido!')
        else:
            valido = True
            return float(numero)
