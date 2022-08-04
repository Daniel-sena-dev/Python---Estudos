numero = int(input('Digite o numero que deseja a tabuada: '))

for contador in range(1, 11):
    print(f'{numero} X {contador} = {contador * numero}')