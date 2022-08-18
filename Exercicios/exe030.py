print('6- Maior numero: ')
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
maior = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
print(f'O maior numero de {numero1}, {numero2} e {numero3} é {maior}')
