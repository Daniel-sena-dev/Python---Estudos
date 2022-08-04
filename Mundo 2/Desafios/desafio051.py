numero = int(input('Digite um numero: '))
razaoPA = int(input('Digite a razão: '))
PA = numero


for contador in range(0, 10):
    print(PA, end='  ↦ ')
    PA += razaoPA


print('ACABOU')