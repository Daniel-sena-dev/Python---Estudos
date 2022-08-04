import time
numero = 0

while True:
    numero = float(input('Digite um numero (numeros negativos finalizam o programa): '))

    if numero < 0:
        print('Finalizando o programa', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        break
    else:
        print('=' * 10)
        print(f'TABUADA DO NUMERO {numero}')
        contador = 1
        while contador < 11:
            print(f'{contador} X {numero} = {contador * numero:.02f}')
            contador += 1
