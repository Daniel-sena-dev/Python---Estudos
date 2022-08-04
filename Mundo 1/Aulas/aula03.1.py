numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
restoDivisao = numero1 % numero2
divisaoInteira = numero1 // numero2
exponenciacao = numero1 ** numero2

print(f'Os numeros digitados foram {numero1} e {numero2}')
print(f'A soma é igual a {soma}')
print(f'A subtração é {subtracao}')
print(f'A divisão é {divisao}')
print(f'A multiplicação é {multiplicacao}')
print(f'O resto da divisão {restoDivisao}')
print(f'O a divisão inteira é {divisaoInteira}')
print(f'A exponeciação é de {exponenciacao:.3f}')
