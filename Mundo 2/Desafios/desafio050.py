soma = 0
for contador in range(1, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma += numero

print(f'O valor dos numeros pares foi de {soma}')