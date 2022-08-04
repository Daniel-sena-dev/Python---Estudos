numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

if (numero1 > numero2 and numero1 > numero3):
    print(f'O mairo numero é {numero1}')
if (numero2 > numero1 and numero2 > numero3):
    print(f'O maior numero é o {numero2}')
if (numero3 > numero1 and numero3 > numero2):
    print(f'O maior numero é o {numero3}')

if (numero1 < numero2 and numero1 < numero3):
    print(f'O menor numero é {numero1}')
if (numero2 < numero1 and numero2 < numero3):
    print(f'O menor numero é o {numero2}')
if (numero3 < numero1 and numero3 < numero2):
    print(f'O menor numero é o {numero3}')

