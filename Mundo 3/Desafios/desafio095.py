jogadorDados = dict()
jogadores = list()
gol = list()
partidas = 0
total = 0

while True:
    total = 0
    jogadorDados['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogadorDados["nome"]} jogou? '))
    for contador in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {contador+1}? ')))

    jogadorDados['gols'] = gol[:]

    for contador in range(0, len(gol)):
        total += gol[contador]

    jogadorDados['total'] = total
    jogadores.append(jogadorDados.copy())
    gol.clear()

    #continuar
    while True:
        continuar = input('Quer continuar? [S/N] ').upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('VALOR INVALIDO')
    if continuar == 'N':
        print('ENCERRANDO O PROGRAMA...')
        break
print('-=-' * 10)
print('cod nome      gols       total')
print('-'*40)
for contador, lista in enumerate(jogadores):
    print(contador, end=' ')
    for chaves, valores in lista.items():
        print(f'{valores}', end='     ')
    print('')

# MOSTRAR DADO DE QUAL JOGADOR?
while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}')

    for i, v in enumerate(jogadores[dados]['gols']):
        print(f'     => Na partida {i}, fez {v} gols.')
    print(f'Foi um total de {jogadores[dados]["total"]} gols.')

    # continuar
    while True:
        continuar = input('Quer continuar? [S/N] ').upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('VALOR INVALIDO')
    if continuar == 'N':
        print('ENCERRANDO O PROGRAMA...')
        break
