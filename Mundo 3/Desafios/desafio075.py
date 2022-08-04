
numeros = (int(input('digite primerio numero: ')), int(input('digite o segundo numero: ')),
           int(input('digite o terceiro numero: ')), int(input('digite o quarto numero: ')))

#A) quantas vezes apareceu o valor 9
print(f'O número 9 apareceu {numeros.count(9)} vezes')

#B) em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

#C) quais foras os numeros pares:
print(f'Os valores pares digitados foram ', end='')
pares = 0
for contador in range(0, 4):
    if numeros[contador] % 2 == 0 and numeros[contador] != 0:
        print(numeros[contador], end=' ')
        pares += 1

if pares == 0:
    print('nenhum')