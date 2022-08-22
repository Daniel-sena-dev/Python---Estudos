print('19- programa para ler um numero inteiro')
numero = int(input('Digite um numero menor que 1000: '))
centena = dezena = unidade = numCopy = 0

if 0 < numero < 1000:
    numCopy = numero
    if numero // 100:
        centena = numero // 100
        dezena = numero % 100
        numero = numero % 100
    if numero // 10:
        dezena = numero // 10
        unidade = numero % 10
        numero = numero % 10
    if numero // 1:
        unidade = numero

print(f'O numero {numCopy} tem {centena} centena, {dezena} dezena e {unidade} unidade')
