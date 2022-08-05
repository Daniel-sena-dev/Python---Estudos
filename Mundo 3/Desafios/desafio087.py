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

print('-=-'*10)
for contador in matriz:
    print(contador)
print('-=-'*10)

# A) soma dos valores pares
par = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
print(f'A soma dos valores pares é de {par}')

# B) A soma da terceira coluna
soma = linha1[2] + linha2[2] + linha3[2]

print(f'A soma dos valores da terceira coluna é {soma}')

# C) O maior valor da segunda linha é:
maior = 0
for linha in linha2:
    if linha > maior:
        maior = linha
print(f'O maior valor da segunda linha é {maior}')