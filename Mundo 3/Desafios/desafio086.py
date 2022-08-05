#matriz
matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()

for contador in range(0, 3):
    linha1.append(int(input(f'Digite o valor para [0, {contador}]: ')))
matriz.append(linha1)
for contador in range(0, 3):
    linha2.append(int(input(f'Digite o valor para [1, {contador}]: ')))
matriz.append(linha2)
for contador in range(0, 3):
    linha3.append(int(input(f'Digite o valor para [2, {contador}]: ')))
matriz.append(linha3)

for contador in matriz:
    print(contador)
