print('21- Programa para saber se o numero digitado é primo ou não: ')
numero = int(input('Digite um numero: '))
primo = 0

for cont in range(1, numero + 1):
    if numero % cont == 0:
        primo += 1

if primo == 2:
    print(f'O numero {numero} é primo!')
else:
    print(f'O numero {numero} não é primo!')
