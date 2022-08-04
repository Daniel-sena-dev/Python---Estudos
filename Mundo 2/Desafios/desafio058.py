import random

numeroJogador = -1
numeroPC = random.randint(0, 10)
palpites = 0

print('=' * 55)
print('TENTE ADIVINHAR QUAL NUMERO EU PENSEI DE 0 A 10')
print('=' * 55)

while numeroJogador != numeroPC:
    numeroJogador = int(input('Digite o numero que pensei: '))
    if numeroJogador != numeroPC:
        if numeroJogador > numeroPC:
            print(f'\033[1;31mCHUTOU MUITO LONGE! numero digitado {numeroJogador}\033[m')
        else:
            print(f'\033[1;31mCHUTOU FRACO! numero digitado {numeroJogador}\033[m')
    else:
        print(f'\033[1;32mDROGA VOCÊ ACERTOU! PENSEI NO NUMERO {numeroPC}\033[m')

    palpites += 1

print('VOCE GANHOU!')
print(f'Voce precisou de \033[1;34m{palpites}\033[m tentativas!')