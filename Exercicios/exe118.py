print(f'15- programa para calcular de notas de alunos: ')
nota = soma = maiorMedia = menorSete = 0
notas = list()
saida = False

while True:
    if saida:
        break

    while True:
        try:
            nota = float(input('Digite a nota do aluno: (numeros negativos encerra o programa!)'))
        except ValueError:
            print('ERRO! VALOR INVALIDO')
        else:
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            elif nota < 0:
                saida = True
                break
            else:
                print('ERRO! Valor invalido!')


print(f'A quantidade de notas foi {len(notas)}')
print('As notas foram ', end='')
for cont in notas:
    print(f'{cont}', end=', ')
print('')
for cont in range(len(notas), -1):
    print(f'As notas foram: {cont}')
print('')
for cont in range(0, len(notas)):
    soma += notas[cont]
print(f'O total da nota foi {soma:.02f}')
print(f'A media das notas foi {soma/len(notas):.02f}')
for cont in range(0, len(notas)):
    if notas[cont] > soma/len(notas):
        maiorMedia += 1

    if notas[cont] < 7:
        menorSete += 1
print(f'As notas maiores que a media foi {maiorMedia}')
print(f'As notas menores que sete foi {menorSete}')
print('O programa foi encerrado!')