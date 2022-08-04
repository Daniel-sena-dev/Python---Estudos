import math

comprimentoOposto = float(input('Digite o comprimento do cateto oposto: '))
comprimentoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(comprimentoOposto, comprimentoAdjacente)
#(math.sqrt(math.pow(comprimentoOposto, 2) + math.pow(comprimentoAdjacente, 2)))

print(f'O valor do cateto oposto é de {comprimentoOposto} e do cateto adjacente é de {comprimentoAdjacente}, o valor da hipotenusa é igual á A = {hipotenusa:.02f}')
