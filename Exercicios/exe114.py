print('12- Programa para verificar quais alunos tem a altura menor que a media da turma: ')
idades = list()
alturas = list()
media = 0
quantidadeAlunos = int(input('Digite a quantidade de alunos: '))
menorMedia = 0

for cont in range(0, quantidadeAlunos):
    idades.append(int(input('Digite a idade: ')))
    alturas.append(float(input('Digite a altura: ')))
    media += alturas[cont]

media /= quantidadeAlunos
for cont in range(0, quantidadeAlunos):
 if idades[cont] > 13:
    if alturas[cont] > media:
        menorMedia += 1

print(f'A quantidade de alunos com mais de 13 anos e com altura menor que a media da turma foi: {menorMedia}')
