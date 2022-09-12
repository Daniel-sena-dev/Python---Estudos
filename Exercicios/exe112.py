print('10- criar duas listas: ')
lista1 = list()
lista2 = list()
lista3 = list()
contadorLista1 = 0
contadorLista2 = 0

for cont in range(0, 10):
    lista1.append(int(input('Digite um numero: ')))

for cont in range(0, 10):
    lista2.append(int(input('Digite um numero: ')))

for cont in range(0, 20):
    if cont % 2 == 0:
        lista3.append(lista1[contadorLista1])
        contadorLista1 += 1
    else:
        lista3.append(lista2[contadorLista2])
        contadorLista2 += 1

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')
