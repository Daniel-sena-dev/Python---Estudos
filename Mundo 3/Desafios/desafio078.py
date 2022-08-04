listaNum = []

for contador in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para a posição {contador}: ')))
print('-=-' * 10)
print(f'Você digitou {listaNum}')
maior = max(listaNum)
menor = min(listaNum)
tamanho = len(listaNum)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for contador in range(0, tamanho):
    if listaNum[contador] == maior:
        print(f'{contador}...', end=' ')

print('')

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for contador in range(0, tamanho):
    if listaNum[contador] == menor:
        print(f'{contador}...', end=' ')







