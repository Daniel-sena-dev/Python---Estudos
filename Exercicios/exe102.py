print('50- Programa para calcular uma serie de numeros: ')
termoFinal = int(input('Digite o numero final: '))
soma = 0

for cont in range(1, termoFinal + 1):
    if cont == 1:
        print(f'1 + ', end=' ')
    elif 1 < cont < termoFinal:
        print(f'1/{cont} + ', end=' ')
    else:
        print(f'1/{cont} = ', end=' ')
    soma += 1/cont
print(f'{soma:.02f}')
