print('10- Programa para receber dois numero inteiros e printar os valores entre eles: ')
inicio = int(input('Digite o numero para começar: '))
fim = int(input('Digite o numero final: '))

if inicio < fim:
    for cont in range(inicio, fim + 1):
        print(cont, end=' ')
else:
    for cont in range(inicio, fim - 1, -1):
        print(cont, end=' ')
