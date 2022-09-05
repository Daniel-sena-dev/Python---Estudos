print('24- programa para calcular mediaVeiculos aritmetica de N notas: ')
quantidadeNotas = int(input('Digite a quantidade de notas: '))
notas = 0

for cont in range(0, quantidadeNotas):
    notas += float(input('Digite uma nota: '))

media = notas / quantidadeNotas
print(f'A mediaVeiculos foi: {media:.02f}')
