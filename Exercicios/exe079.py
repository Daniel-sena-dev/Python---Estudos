print('27- Programa para organizar quantTurmas: ')
quantTurmas = int(input('Digite a quantidade de quantTurmas: '))
turmas = list()
mediaAlunos = 0

for cont in range(0, quantTurmas):
    while True:
        try:
            quantAlunos = int(input('Digite a quantidade de alunos (não ultrapassar 40): '))
        except ValueError:
            print('Erro! valor digitado invalido')
        else:
            if 0 < quantAlunos <= 40:
                turmas.append(quantAlunos)
                break
            else:
                print('Valor digitado invalido!')

print(f'A quantidade de turmas foi {quantTurmas}: ')
for cont in range(0, quantTurmas):
    print(f'A turma {cont + 1} tem {turmas[cont]} alunos')
    mediaAlunos += turmas[cont]
print(f'A media de alunos foi {mediaAlunos/quantTurmas:.02f}')
    