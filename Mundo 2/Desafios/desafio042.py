reta1 = int(input('Digite o primeiro segmento de reta: '))
reta2 = int(input('Digite o segundo segmento de reta: '))
reta3 = int(input('Digite o terceiro segmento de reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 and reta1 == reta3:
        print(f'Esses segmentos de retas A={reta1}, B={reta2} e C={reta3}. formam um triangulo EQUILATERO.')
    elif reta1 == reta2 or reta1 == reta3:
        print(f'Esses segmentos de retas A={reta1}, B={reta2} e C={reta3}. formam um triangulo ISOSCELES.')
    else:
        print(f'Esses segmentos de retas A={reta1}, B={reta2} e C={reta3}. formam um triangulo ESCALENO.')
else:
    print('Não pode formar um triangulo')