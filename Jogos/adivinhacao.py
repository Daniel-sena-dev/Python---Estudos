# JOGO DE ADIVINHAÇÃO
import random
import time

print('-' * 21)
print(f'{" JOGO DE ADIVINHAÇÃO"}')
print('-' * 21)
numeroSorteado = random.randint(0, 10)
tentativas = 0
while True:
    # Validação do número digitado
    while True:
        try:
            numeroDigitado = int(input('Digite o número: '))
        except ValueError:
            print('ERRO! Digite um numero inteiro valido')
        else:
            if numeroDigitado > 10:
                print('ERRO! Digite um valor menor ou igual a 10')
                continue
            if numeroDigitado < 0:
                print('ERRO! Digite um valor maior ou igual a 0')
                continue
            else:
                break

    # Checando se o jogador acertou
    if numeroDigitado == numeroSorteado:
        print(f'Parabéns! você acertou o numero que eu pensei')
        tentativas += 1
        break
    else:
        if numeroDigitado > numeroSorteado:
            print(f'Você errou! chutou muito alto!')
            tentativas += 1
        else:
            print(f'Você errou! chutou muito baixo!')
            tentativas += 1

time.sleep(1)
print('-' * 30)
time.sleep(1)
print('PARABENS! VOCÊ GANHOU O JOGO!')
time.sleep(1)
print(f'O número sorteado foi: {numeroSorteado}')
time.sleep(1)
print(f'O seu número de tentativas foi de: {tentativas}')
time.sleep(1)
print('-' * 30)
