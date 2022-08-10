def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL
num = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {num}')
