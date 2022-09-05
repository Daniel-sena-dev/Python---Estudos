print('8- Programa para ler 5 numero e somar e fazer a mediaVeiculos dos numeros: ')
soma = num = 0

for cont in range(0, 5):
    num = int(input('Digite um numero: '))
    soma += num

print(f'A soma dos numeros foram {soma}, e a mediaVeiculos foi {soma/5}')
