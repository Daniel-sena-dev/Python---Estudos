listaNumeros = []
pares = []
impares = []

while True:
    listaNumeros.append(int(input('Digite um numero: ')))

    # QUER CONTINUAR? =======================================
    continuar = input('Quer continuar? [S/N] ').upper()
    while continuar != 'S' and continuar != 'N':
        print('Valor invalido! digite novamente')
        continuar = input('Quer continuar? [S/N] ').upper()

    if continuar == 'N':
        break
print('-=-' * 10)
tamanho = len(listaNumeros)
#===============================================
for contador in range(0, tamanho):
    if listaNumeros[contador] % 2 == 0:
        pares.append(listaNumeros[contador])
    else:
        impares.append(listaNumeros[contador])
print('-=-' * 10)
print(f'Os valores digitados foram {listaNumeros}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')