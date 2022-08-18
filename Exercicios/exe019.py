import math

print(f'11- Pedir dois numeros inteiros e um real: ')
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = float(input('Digite um numero: '))
print('A- o produto do dobro do primeiro com a metade do segundo')
a = (math.pow(numero1, 2) * (numero2/2))
print(a)
print('B- a soma do triplo do primeiro com o terceiro')
b = (numero1 * 3) + numero3
print(b)
print('C- terceiro elevado ao cubo')
c = (math.pow(numero3, 3))
print(c)
