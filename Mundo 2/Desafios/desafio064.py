import time
numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um numero: (digite \033[1m[999]\033[m para sair do programa) '))
    if numero != 999:
        soma += numero
        contador += 1
    else:
        print('Programa encerrado!', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')


print(f'A quantidade de numeros digitados foi de {contador} e a soma é de {soma}')
