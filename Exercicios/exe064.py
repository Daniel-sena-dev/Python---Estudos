print('12- Tabuada 1.0v: ')
numero = int(input('Digite um numero para ver sua tabuada: '))
print(f'Tabuada de {numero}:')
for cont in range(1, 11):
    print(f'{numero} X {cont} = {numero * cont}')
    