listaNumeros = []
quantNumero = 0

while True:
    listaNumeros.append(int(input('Digite um numero: ')))

    # A Quantidade numeros
    quantNumero += 1

    # QUER CONTINUAR? =======================================
    continuar = input('Quer continuar? [S/N] ').upper()
    while continuar != 'S' and continuar != 'N':
        print('Valor invalido! digite novamente')
        continuar = input('Quer continuar? [S/N] ').upper()

    if continuar == 'N':
        break

# A quantidade de numeros digitado
print(f'A quantidade de numeros digitados foi {quantNumero}')

# B lista de valores:
listaNumeros.sort(reverse=True)
print(f'A lista de valores na ordem decrescente é {listaNumeros}')

# C se o valor 5 foi digitado
if 5 in listaNumeros:
    print('O valor 5 está na lista ')
else:
    print('O valor 5 não está na lista')