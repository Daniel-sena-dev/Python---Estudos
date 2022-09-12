print('6- programa que pede 4 notas de 10 alunos: ')
notas = list()
media = 0
acimaMedia = 0

for cont in range(0, 10):
    for cont2 in range(0, 4):
        notas.append(float(input(f'Digite a nota do aluno {cont + 1}: ')))
        media += notas[cont2]

    media /= 4

    if media > 7:
        acimaMedia += 1

    notas.clear()
    media = 0

print(f'O numero de alunos com medias acima de 7 foi {acimaMedia}')
