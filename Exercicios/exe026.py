print('2- Programa para mostar se o numero é positivo ou negativo')
numero = float(input('Digite um numero: '))

if numero > 0:
    print(f'O {numero} é positivo!')
elif numero < 0:
    print(f'O {numero} é negativo!')
else:
    print(f'O {numero} é nulo')
