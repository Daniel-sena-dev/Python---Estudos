print('49- Programa para calcular uma serei de termos: ')
numeroFinal = int(input('Digite o numero final: '))
soma = 0
termo2 = 1

print('S = ', end=' ')
for cont in range(1, numeroFinal + 1):
    if cont < numeroFinal:
        print(f'{cont}/{termo2} + ', end=' ')
    else:
        print(f'{cont}/{termo2} = ', end=' ')
    soma += cont / termo2
    termo2 += 2
print(f'{soma:.02f}')
