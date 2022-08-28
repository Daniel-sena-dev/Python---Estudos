print('14- programa que peça 10 numero inteiros, mostre a quantidade de numeros pares e quantidade de impares: ')
pares = impares = num = 0

for cont in range(0, 10):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'A quantidade de pares digitados é {pares} e {impares} impares')
