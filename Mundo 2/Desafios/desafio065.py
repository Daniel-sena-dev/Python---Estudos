import  time
continuar = 'S'
contador = 0
media = 0
maior = 0
menor = 0
numero = 0
somaTotal = 0

while continuar != 'N':
    numero = int(input('Digite um numero: ')) #pedindo um numero
    contador += 1  # quantos numeros foram digitados
    somaTotal += numero #soma total dos numero digitados

    #Definindo os maiores e menores
    if contador == 1: #se for o primeiro numero ele é colocado como maior e menor
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero
    #================================

    continuar = input('Você deseja continuar? digite [S] para continuar ou [N] para encerrar o programa ').upper()

    while continuar != 'S' and continuar != 'N':
        print('\033[1;32mValor digitado invalido! digite novamente\033[m')
        continuar = input('Você deseja continuar? digite [S] para continuar ou [N] para encerrar o programa ').upper()


    if continuar == 'N':
        print('Encerrando o programa', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')


media = somaTotal/contador

print(f'A quantidade de numeros digitados foi de {contador} a media foi {media:.02f}, o maior numero foi {maior} e o menor numero {menor}')