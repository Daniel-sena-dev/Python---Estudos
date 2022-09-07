print('3- Programa para ler 4 notas e mostrar a media: ')
notas = list()
media = 0

for cont in range(0, 4):
    notas.append(float(input('Digite a nota: ')))
    media += notas[cont]

print(f'A media foi de {media/4:.02f}')
