print('5- Programa para população de um país 2.0v: ')
cidadeA = int(input('Digite a quantidade de pessoas da cidade A: '))
cidadeB = int(input('Digite a quantidade de pessoas da cidade B: '))
taxaCrescimentoA = float(input('Digite a taxa de crescimento da cidade A: '))
taxaCrescimentoB = float(input('Digite a taxa de crescimento da cidade B: '))
anos = 0

while cidadeA < cidadeB:
    cidadeA += cidadeA * taxaCrescimentoA
    cidadeB += cidadeB * taxaCrescimentoB
    anos += 1

print(f'Foi necessario {anos} anos para a cidade A ultrapassar ou igualar a cidade B')
