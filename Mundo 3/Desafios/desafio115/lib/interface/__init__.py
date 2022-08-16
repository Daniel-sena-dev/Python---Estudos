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


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
