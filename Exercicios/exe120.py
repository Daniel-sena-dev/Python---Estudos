print('17- Desafio de competição de salto em distancia: ')
saltos = list()
media = 0
while True:
    nomeAtleta = str(input('Digite o nome do atleta: '))
    # saindo do programa ao nao digitar o nome do atleta
    if nomeAtleta == '':
        break

    for cont in range(0, 5):
        saltos.append(float(input(f'Digite o numero do salto {cont + 1}º: ')))
        media += saltos[cont]
    print('Resultado final: ')
    print(f'Atleta: {nomeAtleta}')

    print('Saltos: ', end='')
    for cont in range(0, 5):
        if cont < 4:
            print(f'{saltos[cont]:.02f}', end=' - ')
        else:
            print(f'{saltos[cont]:.02f}')
    print(f'A media do atleta foi: {media/5:.02f}m')

    #limpando a lista e media
    saltos.clear()
    media = 0