print('13- Programa para ler dois numero, base e expoente e mostre o primeiro numero elevado ao segundo: ')
base = int(input('Digite a base: '))
expoente = int(input('Digite a expoente: '))
resultado = base

for cont in range(1, expoente):
    resultado *= base
print(f'A potencia com base {base} e expoente {expoente} é {resultado}')
