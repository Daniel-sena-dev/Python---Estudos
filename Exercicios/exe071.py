print('19- Programa que mostre a soma de uma lista, max e min: 2.0v')
quantidadeNumeros = int(input('Digite a quantidade de numeros: '))
lista = list()
for contador in range(0, quantidadeNumeros):
    while True:
        try:
            numero = (int(input('Digite um numero: digite apenas numeros entre 0 e 1000 ')))
        except ValueError:
            print('ERRO! valor digitado invalido!')
        else:
            if 0 <= numero <= 1000:
                lista.append(numero)
                break
            else:
                print('Valor digitado invalido! digite apenas numeros entre 0 e 1000')

soma = 0
for cont in lista:
    soma += cont

print(f'O maior numero da lista é {max(lista)}, o menor numero é {min(lista)} e a soma dos valores é {soma}')