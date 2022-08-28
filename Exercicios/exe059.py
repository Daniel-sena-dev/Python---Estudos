print('7- programa para ler 5 numeros e mostrar o maior: ')
lista = list()

for cont in range(0, 5):
    lista.append(int(input('Digite um numero: ')))

print(max(lista))
