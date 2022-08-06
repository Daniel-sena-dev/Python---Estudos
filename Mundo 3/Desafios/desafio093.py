dadosJogador = dict()

dadosJogador['nome'] = input('Nome do Jogador: ')
quantPartidas = int(input(f'Quantas partidas {dadosJogador["nome"]} jogou? '))
gol = list()
totalGols = 0
for contador in range(0, quantPartidas):
    gol.append(int(input(f'Quantos golf na partida {contador + 1}? ')))
    totalGols += gol[contador]
dadosJogador['gols'] = gol[:]
dadosJogador['total'] = totalGols
print('-=-' * 10)
print(dadosJogador)
print('-=-' * 10)
for chaves, valores in dadosJogador.items():
    print(f'O campo {chaves} tem o valor {valores}')
print('-=-' * 10)
print(f'O jogador {dadosJogador["nome"]} jogou {quantPartidas}.')
for contador, rodada in enumerate(gol):
    print(f'=> Na partida {contador}, fez {rodada} gols.')

print(f'Foi um total de {dadosJogador["total"]} gols')
