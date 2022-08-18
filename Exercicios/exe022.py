import math

print('16 - Programa para loja de tintas')
areaSerPintada = float(input('Digite a area a ser pintada: '))
coberturaTinta = 3
lataTintas = (areaSerPintada/coberturaTinta)
print(f'Você precisa de {lataTintas:.02f}Litros.')
if lataTintas == 18 or lataTintas < 18:
    print(f'Você precisará de apenas uma lata de tinta! o valor é de R$80,00')
elif lataTintas > 18:
    totalLatas = lataTintas / 18
    restoLatas = 18 / lataTintas
    print(f'Você vai precisar de {math.ceil(totalLatas)} latas de tinta que vai custar R${math.ceil(totalLatas) * 80:.02f}')
