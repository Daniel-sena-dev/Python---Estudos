listaGeral = list()
par = list()
impar = list()

for contador in range(0, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
listaGeral.append(par[:])
listaGeral.append(impar[:])

print(f'Os valores pares digitados foram: {sorted(listaGeral[0])}')
print(f'Os valores impares digitados foram: {sorted(listaGeral[1])}')
