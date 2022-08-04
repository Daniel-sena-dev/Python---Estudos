numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
continuar = ''
print('=' * 10)
while True:
    numeroDigitado = int(input('Digite um numero entre 0 e 20: '))

    while numeroDigitado < 0 or numeroDigitado > 20:
        print('Numero digitado invalido. digite novamente')
        numeroDigitado = int(input('Digite um numero entre 0 e 20: '))

    print(f'O numero digitado foi {numeros[numeroDigitado]}')
    print('=' * 10)
    continuar = input('Deseja continuar? digite sim ou não [S/N]').upper()
    while continuar != 'S' and continuar != 'N':
        print('VALOR DIGITADO INVALIDO. DIGITE NOVAMENTE')
        continuar = input('Deseja continuar? digite sim ou não [S/N]').upper()

    if continuar == 'N':
        break
