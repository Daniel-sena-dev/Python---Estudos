primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
PA = primeiroTermo
contador = 10

while contador > 0:
    print(f'{PA}', end=' -> ')
    PA += razao
    contador -= 1

print('Acabou')