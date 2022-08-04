primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
PA = primeiroTermo
termos = 11

while termos != 0:
    if termos > 1:
        print(f'{PA}', end=' -> ')
        PA += razao
        termos -= 1
    elif termos == 1:
        print('\n')
        print('\033[1mDigite a quantidade de termos que você deseja ou digite [0] para finalizar\033[m')
        termos = int(input('Digite: '))

print('PROGRAMA FINALIZADO!')
