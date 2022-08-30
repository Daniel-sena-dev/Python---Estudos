import time
print('20- calculo fatorial 2.0v: ')
while True:
    # tratando entrada de dados:
    saida = False
    while True:
        try:
            numero = int(input('Digite um numero entre 0 e 16: (digite 999 para sair) '))
        except ValueError:
            print('ERRO! Digite um valor válido!')
        else:
            if numero == 999:
                saida = True
                break
            elif 0 < numero <= 16:
                break
            else:
                print('Valor digitado inválido!')
    if saida:
        print('finalizando o programa ', end='')
        for cont in range(0, 3):
            time.sleep(0.5)
            print('.', end='')
        break

    print(f'{numero}! = ', end='')
    fatorial = 1
    inicio = numero
    for cont in range(inicio, 0, -1):
        if cont > 1:
            print(f'{numero} x ', end='')
        else:
            print(f'{numero} = ', end='')
        fatorial *= numero
        numero -= 1
    print(f'{fatorial}')
