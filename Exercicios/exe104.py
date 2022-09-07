print('2- Programa para ler 10 numeros reais e mostrar na ordem inversa: ')
lista = list()

for cont in range(0, 10):
    lista.append(float(input('Digite um numero: ')))

for cont in range(9, -1, -1):
    print(lista[cont], end=' ')
