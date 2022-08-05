import time

alunos = list()
aluno = list()
notas = list()
media = 0
continuar = ''

while True:
    aluno.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1])/2
    notas.append(media)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()

    continuar = input('Deseja continuar? digite sim ou não [S/N] ').upper()
    while continuar != 'S' and continuar != 'N':
        print('VALOR INVALIDO')
        continuar = input('Deseja continuar? digite sim ou não [S/N] ').upper()
    if continuar == 'N':
        break


print('-=-'*20)
print('No. NOME MÉDIA')
print('-' * 20)

for contador in range(0, len(alunos)):
    print(f'{contador}  {alunos[contador][0]} {alunos[contador][1][2]}')
print('-' * 20)

while True:
    opcao = int(input('Mostrar as notas de qual aluno? (999) interrompe: '))

    if opcao == 999:
        print('FINALIZANDO', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        break

    print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1][0:2]} ')
    print('-' * 20)
print('')
print('<<< VOLTE SEMPRE >>>')
