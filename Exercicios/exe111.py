print('9- Programa que leia um vetor acom 10 numeros inteiros: ')
lista = list()
soma = 0
for cont in range(0, 10):
    lista.append(int(input('Digite um numero: ')))
    soma += lista[cont] ** 2

print(f'A soma dos quadrados é {soma}')

