import math
print('17 - Programa para loja de tintas 2.0v')
areaSerPintada = float(input('Digite o tamanho da parede a ser pintada: '))
cobertura = 6
parede = areaSerPintada / cobertura
print(f'TOTAL LATAS:')
total18 = parede // 18
resto = parede % 18

print(f'O total de latas de 18 litros é de {total18}')

total032 = resto % 3.2
print(f'O total de latas de 3,2 litros é de {math.ceil(total032)}')
print(f'O valor total das compras é de R${(math.ceil(total18) * 80) + (math.ceil(total032) * 25):.02f}')
