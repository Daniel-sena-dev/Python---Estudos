import time

print('45- Correção de gabarito 1.0v: ')
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
media = acertos = resposta = totalAlunos = 0
listaNotas = list()
gabaritoAluno = list()
sair = False

while True:
    if sair:
        time.sleep(0.5)
        print('Finalizando', end='')
        for cont in range(0, 3):
            time.sleep(0.5)
            print('.', end='')
        print('')
        break

    for cont in range(0, 10):
        while True:
            try:
                resposta = str(input(f'Digite a resposta da pergunta {cont + 1}: ')).upper()[0]
            except ValueError:
                print('ERRO! Valor invalido!')
            else:
                if resposta in 'ABCDE':
                    gabaritoAluno.append(resposta)
                    break
                else:
                    print('Resposta invalida')

    # COMPARANDO
    for cont in range(0, 10):
        if gabaritoAluno[cont] == gabarito[cont]:
            acertos += 1

    # SAIDA
    media += acertos
    listaNotas.append(acertos)
    totalAlunos += 1
    acertos = 0
    gabaritoAluno.clear()

    # FINALIZANDO O PROGRAMA
    while True:
        try:
            finalizar = str(input('Deseja finalizar o programa? [S/N]')).upper()[0]
        except ValueError:
            print('Erro! Valor invalido')
        else:
            if finalizar == 'S':
                sair = True
                break
            else:
                break

print(f'O maior acerto foi {max(listaNotas)} e o menor foi {min(listaNotas)}')
print(f'O total de alunos que usou foi {totalAlunos}')
print(f'A media de acertos foi {media/totalAlunos}')
