import random
import time
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)

numeroJogador = numeroPC = 0
parImpar = ''
soma = 0
ganhou = 0

while True:
    numeroJogador = int(input('Digite um numero: '))
    #validando o numero
    while numeroJogador < 0:
        print('\033[1;32mERRO NUMERO INVALIDO\033[m')
        print('\033[1;32mDigite um numero positivo\033[m')
        numeroJogador = int(input('Digite um numero: '))

    parImpar = input('Par ou ímpar [P/I]? ').upper()
    #validando o valor
    while parImpar != 'P' and parImpar != 'I':
        print('\033[1;32mERRO VALOR INVALIDO\033[m')
        print('\033[1;32mDigite [P/I]\033[m')
        parImpar = input('Par ou ímpar [P/I]? ').upper()

    #PC escolhendo o numero
    numeroPC = random.randint(0, 10)
    print(numeroPC)
    soma = numeroJogador + numeroPC

    #DEFININDO O GANHADOR
    if soma % 2 == 0 and parImpar == 'P':
        ganhou += 1
        print('=' * 20)
        print(f'Você jogou {numeroJogador} e o computador {numeroPC}. Total de {soma} \033[1;34mDEU PAR\033[m!')
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
    elif soma % 2 == 1 and parImpar == 'I':
        ganhou += 1
        print('=' * 20)
        print(f'Você jogou {numeroJogador} e o computador {numeroPC}. Total de {soma} DEU \033[1;34mÍMPAR\033[m!')
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
    else:
        print('=' * 20)
        print('VOCÊ PERDEU!')
        print('-=-' * 10)
        break


print(f'\033[1;32mGAME OVER\033[m! Você venceu {ganhou} vezes.')

