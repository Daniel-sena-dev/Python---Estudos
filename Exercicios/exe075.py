print('23- programa para verificar numeros primos de 1 a N: ')
quantidade = int(input('Digite a quantidade de numeros: '))
primos = 0
quantPrimos = 0

for cont in range(1, quantidade + 1):
    for cont2 in range(1, quantidade + 1):
        if cont % cont2 == 0:
            primos += 1
            quantPrimos += 1
    if primos == 2:
        print(f'{cont} é primo')
        quantPrimos += 1
    else:
        print(f'{cont} nao é primo')
    primos = 0

print(f'A quantidade de divisoes feitas foi de {quantPrimos}')
