import math

print('24- programa para tratamento de numero: ')
numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite um numero: '))
operacao = int(input('Digite qual operação deseja fazer: SOMA[0]|SUBTRAÇÃO[1]|MULTIPLIACAÇÃO[2]|DVISÃO[3]: '))
saida = 0

if operacao == 0:
    saida = numero1 + numero2
    print(f'O valor de {numero1} + {numero2} = {saida}')
    if saida % 2 == 0:
        print(f'É um numero par')
    else:
        print(f'É um numero ímpar')

    if saida >= 0:
        print(f'É um numero positivo')
    else:
        print(f'É um numero negativo')

    if math.ceil(saida) == saida:
        print(f'É um numero inteiro')
    else:
        print(f'É um numero decimal')
elif operacao == 1:
    saida = numero1 - numero2
    print(f'O valor de {numero1} + {numero2} = {saida}')
    if saida % 2 == 0:
        print(f'É um numero par')
    else:
        print(f'É um numero ímpar')

    if saida >= 0:
        print(f'É um numero positivo')
    else:
        print(f'É um numero negativo')

    if math.ceil(saida) == saida:
        print(f'É um numero inteiro')
    else:
        print(f'É um numero decimal')
elif operacao == 2:
    saida = numero1 * numero2
    print(f'O valor de {numero1} + {numero2} = {saida:.02f}')
    if saida % 2 == 0:
        print(f'É um numero par')
    else:
        print(f'É um numero ímpar')

    if saida >= 0:
        print(f'É um numero positivo')
    else:
        print(f'É um numero negativo')

    if math.ceil(saida) == saida:
        print(f'É um numero inteiro')
    else:
        print(f'É um numero decimal')
elif operacao == 3:
    try:
        saida = numero1 / numero2
    except ZeroDivisionError:
        print('Não é possivel dividir por zero')
    else:
        print(f'O valor de {numero1} + {numero2} = {saida}')
        if saida % 2 == 0:
            print(f'É um numero par')
        else:
            print(f'É um numero ímpar')

        if saida >= 0:
            print(f'É um numero positivo')
        else:
            print(f'É um numero negativo')

        if math.ceil(saida) == saida:
            print(f'É um numero inteiro')
        else:
            print(f'É um numero decimal')
else:
    print('Valor digitado invalido')