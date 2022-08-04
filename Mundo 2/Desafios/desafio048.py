soma = 0
contador = 0

for contagem in range(1, 500, 2):
    if contagem % 3 == 0:
        soma += contagem
        contador += 1

print(f'A soma de todos os {contador} numeros impares de 1 até 500 é {soma}')