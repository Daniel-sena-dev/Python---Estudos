#numero aleatorio entre 0 e 5
import random
numero = random.randint(0, 5)
print('-=-' * 20)
numeroDigitado = int(input('Tente adivinhar um numero de 0 a 5: '))
print('-=-' * 20)

if numeroDigitado == numero:
    print(f'Parabens voce acertou o numero que eu pensei!')
else :
    print(f'Você errou tente novamente, eu pensei no numero {numero}')

