def metade(numero, formatacao=True):
    if formatacao:
        return f'R${numero / 2:.02f}'
    else:
        return numero / 2


def dobro(numero, formatacao=True):
    if formatacao:
        return f'R${numero * 2:.02f}'
    else:
        return numero * 2


def aumentando(numero, formatacao=True):
    if formatacao:
        return f'R${numero + (numero * 0.10):.02f}'
    else:
        return numero + (numero * 0.10)


def diminuindo(numero, formatacao=True):
    if formatacao:
        return f'R${numero - (numero * 0.15):.02f}'
    else:
        return numero - (numero * 0.15)


def moeda(numero):
    return f'R${numero:.02f}'


def resumo(numero, aumento, reducao):
    aumentoPorcen = aumento / 100
    reducaoPorcen = reducao / 100
    print('-' * 40)
    print(f'{"RESUMO DO VALOR"}')
    print('-' * 40)
    print(f'Preço analisado:          R$ {numero:.02f}')
    print(f'Dobro do preço:           R$ {numero * 2:.02f}')
    print(f'{aumento}% de aumento:           R$ {numero + (numero * aumentoPorcen):.02f}')
    print(f'{reducao}% de redução:           R$ {numero - (numero * reducaoPorcen):.02f}')
    print('-' * 40)
