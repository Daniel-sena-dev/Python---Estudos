import time

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
operacao = 0

while operacao != 5:
    print(' [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIOR DO PROGRAMA')
    operacao = int(input('Digite qual operação deseja realizar: '))

    if operacao == 1:
        print('OPERAÇÃO SELECIONADA: SOMA')
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif operacao == 2:
        print('OPERAÇÃO SELECIONADA: MULTIPLICAÇÃO')
        print(f'{numero1} X {numero2} = {numero1 * numero2}')
    elif operacao == 3:
        print('OPERAÇÃO SELECIONADA: QUAL É O MAIOR?')
        if numero1 > numero2:
            print(f'O {numero1} é maior que {numero2}.')
        else:
            print(f'O {numero2} é maior que {numero1}.')
    elif operacao == 4:
        print('OPERAÇÃO SELECIONADA: NOVOS NÚMEROS')
        numero1 = int(input('Digite um numero: '))
        numero2 = int(input('Digite um numero: '))
    elif operacao == 5:
        print('FINALIZANDO O PROGRAMA', end = '')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
    else:
        print('\033[1;31mOPERAÇÃO DIGITADA INVALIDA! DIGITE NOVAMENTE\033[m')
