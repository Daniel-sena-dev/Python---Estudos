numero = int(input('Digite um numero: '))
fatorial = 1

print(f'{numero}! =', end=' ')
while numero != 0:
    if numero != 1:
        print(f'{numero} x', end=' ')
        fatorial = numero * fatorial
        numero -= 1
    else:
        print(f'{numero} =', end=' ')
        fatorial = numero * fatorial
        numero -= 1
print(fatorial)
