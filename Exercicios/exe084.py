print('32- Calculo de fatorial: ')
numero = int(input('Digite um numero: '))
total = 1
print(f'{numero}! = ', end='')
for cont in range(numero, 0, -1):
    if cont > 1:
        print(f'{cont} * ', end='')
    else:
        print(f'{cont} = ', end='')
    total *= cont

print(f'{total}')
