print('42- Programa para ler uma quantidade x de numeros: ')
saida = False
entre025 = entre2650 = entre5175 = entre76100 = 0

while True:
    if saida:
        break

    while True:
        try:
            numero = int(input('Digite um numero (numeros negativos encerram o programa): '))
        except ValueError:
            print('Erro! valor invalido')
        else:
            if 0 <= numero <= 100:
                break
            elif numero < 0:
                saida = True
                break
            else:
                print('Numero invalido!')

    if 0 <= numero <= 25:
        entre025 += 1
    elif 26 <= numero <= 50:
        entre2650 += 1
    elif 51 <= numero <= 75:
        entre5175 += 1
    elif 76 <= numero <= 100:
        entre76100 += 1


print(f'Numero digitados: ')
print(f'Numeros entre 0 - 25: {entre025}')
print(f'Numeros entre 26 - 50: {entre2650}')
print(f'Numeros entre 51 - 75: {entre5175}')
print(f'Numeros entre 76 - 100: {entre76100}')
