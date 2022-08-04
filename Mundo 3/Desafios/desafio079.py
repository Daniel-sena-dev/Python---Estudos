listaNumeros = []

while True:
    #PEDINDO NÚMERO
    listaNumeros.append(int(input('Digite um numero (numeros iguais serão desconsiderado): ')))

    #CHECANDO
    tamanhoLista = len(listaNumeros)
    numeroAtual = len(listaNumeros) - 1

    if tamanhoLista > 1:
        for contador in range(0, numeroAtual):
            if listaNumeros[numeroAtual] == listaNumeros[contador]:
                print('Valor repetido! Não vou adicionar')
                listaNumeros.pop()
                break

    #QUER CONTINUAR? =======================================
    continuar = input('Quer continuar? [S/N]').upper()
    while continuar != 'S' and continuar != 'N':
        print('Valor invalido! digite novamente')
        continuar = input('Quer continuar? [S/N]').upper()

    if continuar == 'N':
        break
    #========================================================

print('-=-' * 10)
print(f'Você digitou os valores {sorted(listaNumeros)}')
