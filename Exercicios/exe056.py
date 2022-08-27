print('4- Programa para população de um país: ')
cidadeA = 80000
cidadeB = 200000
taxaCrescimentoA = 0.03
taxaCrescimentoB = 0.015
anos = 0

while cidadeA < cidadeB:
    cidadeA += cidadeA * taxaCrescimentoA
    cidadeB += cidadeB * taxaCrescimentoB
    anos += 1

print(f'Foi necessario {anos} anos para a cidade A ultrapassar ou igualar a cidade B')
