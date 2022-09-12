print('7- Programa para ler um vetor de 5 numeros inteiros: ')
lista = list()
multiplicacao = 1
soma = 0

for cont in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
    soma += lista[cont]
    multiplicacao *= lista[cont]

print(f'A lista de numeros foi: {lista}')
print(f'O total somado foi {soma} e o total multiplicado foi {multiplicacao}')
