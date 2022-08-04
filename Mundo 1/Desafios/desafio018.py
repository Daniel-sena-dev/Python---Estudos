import math

angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

#RETORNA EM RADIANOS
print(f'O valor do angulo é de {angulo}')
print(f'O valor do seno é de  {seno:.02f}')
print(f'O valor do cosseno é de {coseno:.02f}')
print(f'O valor da tangente é de {tangente:.02f}')
