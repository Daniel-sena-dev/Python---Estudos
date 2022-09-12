print('5- armazenar 20 numeros numa lista: ')
lista = list()
par = list()
impar = list()
listaPar = 0
listaImpar = 0
# PAR
for cont in range(0, 5):
    while True:
        try:
            numero = int(input('Digite um numero par: '))
        except ValueError:
            print(f'ERRO! valor invalido')
        else:
            if numero % 2 == 0:
                par.append(numero)
                break
            else:
                print('Você digitou um numero impar!')

# IMPAR
for cont in range(0, 5):
    while True:
        try:
            numero = int(input('Digite um numero impar: '))
        except ValueError:
            print(f'ERRO! valor invalido')
        else:
            if numero % 2 == 1:
                impar.append(numero)
                break
            else:
                print('Você digitou um numero par!')

# ORGANIZANDO EM LISTA
for cont in range(0, 10):
    if cont % 2 == 0:
        lista.append(par[listaPar])
        listaPar += 1
    else:
        lista.append(impar[listaImpar])
        listaImpar += 1

print(lista)
