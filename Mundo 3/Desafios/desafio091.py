import random
import time
from operator import itemgetter #ver isso

jogadas = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6)
}
ranking = list()
print('Valores sorteados:')
for chaves, valores in jogadas.items():
    print(f'O {chaves} tirou {valores}')
    time.sleep(0.5)

print('')
print('Ranking dos jogadores: ')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for ind, valores in enumerate(ranking):
    print(f'{ind+1}º lugar: {valores[0]} com {valores[1]}')
    time.sleep(0.5)
