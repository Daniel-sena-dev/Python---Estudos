def ficha(nome='', gols='0'):
    if gols == '': gols = 0
    if nome == '':
        print(f'O jogador <desconhecido> fez {gols} gols(s) no campeonato.')
    elif gols == '':
        print(f'O jogador {nome} fez 0 gols(s) no campeanato.')
    else:
        print(f'O jogador {nome} fez {gols} gols(s) no campeanato.')


print('--' * 20)
nomeJogador = input('Nome do Jogador: ')
gol = input('Número de Gols: ')
ficha(nomeJogador, gol)
