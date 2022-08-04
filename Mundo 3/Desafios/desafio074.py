import random

numerosGerados = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
                  random.randint(0, 10), random.randint(0, 10))
print(f'Os numeros sorteados foram: {numerosGerados}')
maior = numerosGerados[0]
menor = numerosGerados[0]

#PARA VER O MAIOR SORTEADO max(tupla)
for contador in range(1, 5):
    if numerosGerados[contador] > maior:
        maior = numerosGerados[contador]

#PARA VER O MENOOR SORTEADO min(tupla)
for contador in range(1, 5):
    if numerosGerados[contador] < menor:
        menor = numerosGerados[contador]

print(f'O maior numero sorteado foi: {maior}')
print(f'O menor numero sorteado foi: {menor}')
