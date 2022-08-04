import time

idade = 0
sexo = ''
pessoas = 1
continuar = ''
maiorIdade = 0
quantHomem = 0
quantMulherVinte = 0

while True:
    print('=' * 40)
    print(f'{pessoas}º PESSOA CADASTRADA')
    idade = int(input('Digite sua idade: '))

    # VERIFICANDO A IDADE
    while 0 > idade > 116:
        print('\033[1;32mIdade digitada invalida! digite novamente\033[m')
        idade = int(input('Digite sua idade: '))

    sexo = input('Digite [F/M] (para masculino ou feminino): ').upper()

    # VERIFICANDO O SEXO
    while sexo != 'F' and sexo != 'M':
        print('\033[1;32mSexo digitado invalido! digite novamente\033[m')
        sexo = input('Digite [F/M] (para masculino ou feminino): ').upper()

    # AUMENTANDO NUMERO DE PESSOAS
    pessoas += 1

    # Verificando dados
    if idade >= 18:
        maiorIdade += 1

    if sexo == 'M':
        quantHomem += 1

    if sexo == 'F' and idade < 20:
        quantMulherVinte += 1

    # QUER CONTINUAR?
    continuar = input('Deseja continuar? digite sim ou não [S/N]').upper()
    # Validando a resposta
    while continuar != 'S' and continuar != 'N':
        print('\033[1;32mValor digitado invalido! digite novamente\033[m')
        continuar = input('Deseja continuar? digite sim ou não [S/N]').upper()

    # Fechando o programa
    if continuar == 'N':
        print('Finalizando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        break

print('=' * 25)
print(f'A quantidade de pessoas cadastradas foi {pessoas}')
print(f'A quantidade de pessoas maiores de idade é {maiorIdade}')
print(f'A quantidade de homens cadastrados foi de {quantHomem}')
print(f'A quantidade de mulheres abaixo de 20 anos cadastradas foi de {quantMulherVinte}')