print('8- Programa para pedir a idade e altura de 5 pessoas: ')
idade = list()
altura = list()

for cont in range(0, 5):
    idade.append(int(input('Digite sua idade: ')))
    altura.append(float(input('Digite sua altura: ')))

for cont in range(0, 5):
    print(f'{cont + 1}º tem idade {idade[cont]}, com altura {altura[cont]:.02f}m')
