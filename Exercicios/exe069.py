print('17- Programa para calcular fatorial: ')
numero = int(input('Digite um numero: '))
inicio = numero
saida = 1
print(f'{numero}! =', end=' ')
for cont in range(inicio, 0, -1):
    saida *= numero
    numero -= 1
    if cont > 1:
        print(cont, end='*')
    else:
        print(cont, end='=')

print(f'{saida}')
