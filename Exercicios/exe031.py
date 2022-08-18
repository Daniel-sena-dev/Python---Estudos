print('6- Menor numero: ')
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
print(f'Entre {numero1}, {numero2} e {numero3} o menor é {menor}')
