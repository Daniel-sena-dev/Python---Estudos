print('41- Programa para calculo de dividas: ')
lista = list()
numerador = valorJuros = juros = 0

while True:
    # Valor da dívida
    lista.append(float(input('Digite o valor da divida: ')))
    numerador += 1

    # Parcelas
    while True:
        try:
            lista.append(int(input('Digite a quantidade de parcelas (1/3/6/9/12): ')))
        except ValueError:
            print(f'Erro! valor digitado invalido')
        else:
            if lista[numerador] == 1 or lista[numerador] == 3 or lista[numerador] == 6 or lista[numerador] == 9 or lista[numerador] == 12:
                numerador += 1
                break
            else:
                print('Valor invalido!')
                lista.pop()

    if lista[1] == 3:
        juros = 0.10
    elif lista[1] == 6:
        juros = 0.15
    elif lista[1] == 9:
        juros = 0.20
    elif lista[1] == 12:
        juros = 0.25
    else:
        juros = 1
    # Valor de juros
    valorJuros = lista[0] * juros

    print(f'Valor da Dívida: R${lista[0]:.02f}')
    print(f'Valor dos Juros: R${valorJuros:.02f}')
    print(f'Quantidade de parcelas: {lista[1]}')
    if lista[1] == 1:
        print(f'Valor da parcela: {lista[0]:.02f}')
    else:
        print(f'Valor da parcela: {(lista[0] + valorJuros)/lista[1]:.02f}')
    lista.clear()
    numerador = 0

