print('18- Programa que mostre a soma de uma lista, max e min: ')
quantidadeNumeros = int(input('Digite a quantidade de numeros: '))
lista = list()
for contador in range(0, quantidadeNumeros):
    lista.append(int(input('Digite um numero: ')))
soma = 0
for cont in lista:
    soma += cont

print(f'O maior numero da lista é {max(lista)}, o menor numero é {min(lista)} e a soma dos valores é {soma}')
