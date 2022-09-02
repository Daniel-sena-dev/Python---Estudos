print('36- Tabuada 2.0v')
numero = int(input('Digite o numero que voce quer a tabuada: '))
inicio = int(input('Digite o inicio da tabuada: '))
fim = int(input('Digite o fim da tabuada: '))

for cont in range(inicio, fim + 1):
    print(f'{numero} x {cont} = {numero * cont}')
