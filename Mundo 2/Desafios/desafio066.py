numero = soma = contador = 0

while True:
    numero = int(input('Digite um numero (999 faz parar): '))

    if numero == 999:
        break

    contador += 1
    soma += numero

print(f'A quantidade de numeros digitados foi {contador} e a sua soma foi de {soma}.')