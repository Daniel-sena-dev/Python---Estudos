numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if(numero1 > numero2):
    print(f'O primeiro valor \033[4m{numero1} é maior que o numero \033[4m{numero2}\033[m')
elif (numero2 > numero1):
    print(f'O segundo valor \033[4m{numero2} é maior que o numero \033[4m{numero1}\033[m')
else:
    print('Não existe valor maior, os dois são iguais')

