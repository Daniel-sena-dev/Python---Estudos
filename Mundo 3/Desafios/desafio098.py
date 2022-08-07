import time


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
        for cont in range(inicio, fim + passo, passo):
            print(f'{cont} ', end='')
            # time.sleep(0.5)
    elif inicio > fim and passo > 0:
        passo *= -1
        for cont in range(inicio, fim + passo, passo):
            print(f'{cont} ', end='')
            #time.sleep(0.5)
    else:
        for cont in range(inicio, fim + passo, passo):
            print(f'{cont} ', end='')
            #time.sleep(0.5)
    print(' FIM! ')


# PROGRAMA PRINCIPAL
print('-=-' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for cont in range(1, 11):
    print(f'{cont} ', end='')
    #time.sleep(0.5)
print(' FIM!')

print('-=-' * 20)
print('Contagem de 10 até 0 de 2 em 2')
for cont in range(10, -1, -2):
    print(f'{cont} ', end='')
    #time.sleep(0.5)
print(' FIM! ')

print('-=-' * 20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
