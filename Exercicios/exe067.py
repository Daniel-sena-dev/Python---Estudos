print('15- Fibonacci 1.0v: ')
numero = int(input('Digite um numero: '))
numAnterior = guarda = 0
proximoNumero = 1
for cont in range(0, numero):
    print(numAnterior, end=' ')
    guarda = proximoNumero
    proximoNumero = numAnterior + proximoNumero
    numAnterior = guarda
