print('4- programa para verificar se a letra é uma vogal ou consoante')
letras = str(input('Digite uma letra: ')).lower()

if letras in 'aeiou':
    print(f'{letras} é uma vogal')
elif letras in 'qwrtypsdfghjklçzxvbnm':
    print(f'{letras} é uma consoante')
else:
    print(f'Entrada invalida')
