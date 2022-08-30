print('22- Programa para saber se o numero digitado é primo ou não: 2.0v ')
numero = int(input('Digite um numero: '))
primo = 0
listaPrimos = list()

for cont in range(1, numero + 1):
    if numero % cont == 0:
        primo += 1
        listaPrimos.append(cont)

if primo == 2:
    print(f'O numero {numero} é primo!')
else:
    print(f'O numero {numero} não é primo! ele é divisivel por {listaPrimos}')
