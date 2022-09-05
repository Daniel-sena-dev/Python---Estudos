print('39- Programa para identificar o aluno mais alto e mais baixo: ')
numeroAluno = list()
alturaAluno = list()

for cont in range(0, 10):
    numeroAluno.append(int(input('Digite o codigo do aluno: ')))
    alturaAluno.append(float(input('Digite a altura do aluno: ')))

maisAlto = alturaAluno.index(max(alturaAluno))
maisBaixo = alturaAluno.index(min(alturaAluno))

print(f'O aluno mais baixo foi {maisBaixo + 1} com {min(alturaAluno)}m e o aluno mais alto foi {maisAlto + 1} com {max(alturaAluno)}m')
