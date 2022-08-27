import math

print('23- Programa para saber se um numero é decimal ou inteiro')
numero = float(input('Digite um numero: '))

if math.ceil(numero) == numero:
    print('é inteiro')
else:
    print('é decimal')

