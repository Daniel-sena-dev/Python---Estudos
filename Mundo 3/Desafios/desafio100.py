import random
import time

numero = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        numero.append(random.randint(0, 20))
        print(f'{numero[cont]} ', end='')
        time.sleep(0.2)
    print('PRONTO!')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {numero}, temos ', end='')
    for cont in range(0, 5):
        if numero[cont] % 2 == 0:
            soma += numero[cont]
    print(f'{soma}')


sorteia()
somaPar()
