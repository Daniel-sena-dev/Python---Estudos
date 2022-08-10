# FUNÇÃO PARA METADE DO VALOR
def metade(numero, formatacao=True):
    if formatacao:
        return f'R${numero / 2:.02f}'
    else:
        return numero / 2


# FUNÇÃO PARA DOBRAR O VALOR
def dobro(numero, formatacao=True):
    if formatacao:
        return f'R${numero * 2:.02f}'
    else:
        return numero * 2


# FUNÇÃO AUMENTA %
def aumentando(numero, formatacao=True):
    if formatacao:
        return f'R${numero + (numero * 0.10):.02f}'
    else:
        return numero + (numero * 0.10)


# FUNÇÃO DIMNUI %
def diminuindo(numero, formatacao=True):
    if formatacao:
        return f'R${numero - (numero * 0.15):.02f}'
    else:
        return numero - (numero * 0.15)


# FUNÇÃO CONVERTER EM REAL
def moeda(numero):
    return f'R${numero:.02f}'


# FUNÇÃO RESUMO REAL VALOR
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


# LÊ INTEIRO
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return num


# LÊ REAL
def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return num
