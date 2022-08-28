print('16- Fibonacci 2.0v: ')
numAnterior = guarda = 0
proximoNumero = 1

while True:
    print(numAnterior, end=' ')
    guarda = proximoNumero
    proximoNumero = numAnterior + proximoNumero
    numAnterior = guarda
    if proximoNumero > 500:
        print(proximoNumero)
        break
