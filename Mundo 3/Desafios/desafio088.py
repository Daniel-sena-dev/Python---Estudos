import random
import time

print('-' * 40)
print(f'JOGA NA MEGA SENA')
print('-' * 40)

lista = list()
jogos = list()
sorteio = int(input('Digite a quantidade de jogos que você quer fazer: '))
total = 1

while total <= sorteio:
    contador = 0
    while True:
        numero = random.randint(1, 60)
        if numero not in jogos:
            jogos.append(numero)
            contador += 1
        if contador >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    total += 1

print('-=-' * 3, f'SORTEANDO {sorteio} JOGOS ', '-=' * 3)
for ind, lis in enumerate(lista):
    time.sleep(1)
    print(f'Jogo {ind+1}: {lis}')
