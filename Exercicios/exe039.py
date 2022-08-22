print('15- Programa para saber qual triangulo é: ')
ladoA = float(input('Digite o tamanho do lado A: '))
ladoB = float(input('Digite o tamanho do lado B: '))
ladoC = float(input('Digite o tamanho do lado C: '))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    if ladoA == ladoB and ladoA == ladoC:
        print('Os três lados são iguais! é um triângulo equilátero')
    elif ladoA == ladoB and ladoA != ladoC:
        print('Tem dois lados iguais! é um triângulo isósceles')
    else:
        print('Os três lados são diferentes! é um triângulo escaleno')
else:
    print('Não é um triângulo')