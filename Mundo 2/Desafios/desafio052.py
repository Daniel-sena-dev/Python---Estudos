numero = int(input('Digite um numero: '))
div = numero
divisores = 0

for contador in range(numero, 0, -1):
    if div % contador == 0:
        print(f'\033[1;34m{contador}\033[m', end=' ')
        divisores += 1
    else:
        print(f'\033[1;33m{contador}\033[m', end=' ')
print('\n')
if divisores > 2:
    print('Não é um numero primo')
else:
    print('É um numero primo')