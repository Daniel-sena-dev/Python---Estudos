listaNumero = []

for contador in range(0, 5):
    numero = int(input('Digite um numero: '))

    if contador == 0 or numero > listaNumero[-1] :
        listaNumero.append(numero)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(listaNumero):
            if numero <= listaNumero[posicao]:
                listaNumero.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('-=-' * 10)
print(f'Os valores digitados em ordem foram {listaNumero} ')