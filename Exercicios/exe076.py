print('24- programa para calcular media aritmetica de N notas: ')
quantidadeNotas = int(input('Digite a quantidade de notas: '))
notas = 0

for cont in range(0, quantidadeNotas):
    notas += float(input('Digite uma nota: '))

media = notas / quantidadeNotas
print(f'A media foi: {media:.02f}')
