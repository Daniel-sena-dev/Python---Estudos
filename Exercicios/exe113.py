print('11- criar duas listas: 2.0v')
lista1 = list()
lista2 = list()
lista3 = list()
lista4 = list()
indicesLista1 = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
indicesLista2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
contadorLista1 = contadorLista2 = contadorLista3 = 0

for cont in range(0, 10):
    lista1.append(int(input('Digite um numero: [1]')))

for cont in range(0, 10):
    lista2.append(int(input('Digite um numero: [2]')))

for cont in range(0, 10):
    lista3.append(int(input('Digite um numero: [3]')))

for cont in range(0, 30):
    if cont in indicesLista1:
        lista4.append(lista1[contadorLista1])
        contadorLista1 += 1
    elif cont in indicesLista2:
        lista4.append(lista2[contadorLista2])
        contadorLista2 += 1
    else:
        lista4.append(lista3[contadorLista3])
        contadorLista3 += 1

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')
print(f'Lista 4: {lista4}')
