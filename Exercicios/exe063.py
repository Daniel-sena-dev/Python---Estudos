print('11- Programa para receber dois numero inteiros e printar os valores entre eles 2.0v:')
inicio = int(input('Digite o numero para começar: '))
fim = int(input('Digite o numero final: '))
soma = 0

if inicio < fim:
    for cont in range(inicio, fim + 1):
        print(cont, end=' ')
        soma += cont
else:
    for cont in range(inicio, fim - 1, -1):
        print(cont, end=' ')
        soma += cont
print(f'A soma é {soma}')
