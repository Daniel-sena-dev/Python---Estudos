import math
print('16- Equação do segundo grau: ')
A = float(input('Digite o valor de A: '))
if A == 0:
    print('Não é uma equação do segundo grau!')
else:
    B = float(input('Digite o valor de B: '))
    C = float(input('Digite o valor de C: '))
    delta = B**2 - 4 * A * C
    if delta < 0:
        print('O delta é negativo! não possui raizes reais!')
    elif delta == 0:
        x1 = (-B + math.sqrt(delta)) / 2 * A
        print(f'O delta é igual a zero! possui apenas uma raiz real {x1}')
    else:
        x1 = (-B + math.sqrt(delta)) / 2 * A
        x2 = (-B - math.sqrt(delta)) / 2 * A
        print(f'O delta é positivo! possui duas raizes reais {x1} e {x2}')
