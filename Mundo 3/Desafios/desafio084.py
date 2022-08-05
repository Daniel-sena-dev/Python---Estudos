dados = list()
pessoas = list()
continuar = ''

while True:
    dados.append(input('Digite um nome: '))
    dados.append(float(input('Digite o peso: Kg ')))
    #VERIFICANDO MAIOR  E MENOR PESO
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    print('-=-' * 10)
    pessoas.append(dados[:])
    dados.clear()

    #CONTINUAR
    continuar = input('Deseja continuar? digite sim ou não [S/N]').upper()
    while continuar != 'S' and continuar != 'N':
        print('VALOR INVALIDO')
        continuar = input('Deseja continuar? digite sim ou não [S/N]').upper()
    if continuar == 'N':
        break

# A) quantidade de pessoas na lista
print(f'A quantidade de pessoas cadastradas foi de: {len(pessoas)}')

# B) Pessoas mais pesadas:
maisPesado = list()
for contador in range(0, len(pessoas)):
    if pessoas[contador][1] == maior:
        maisPesado.append(pessoas[contador][0])

print(f'O menor peso foi de {maior}Kg. Peso de {maisPesado}')

# C) Pessoas mais leves:
maisLeves = list()
for contador in range(0, len(pessoas)):
    if pessoas[contador][1] == menor:
        maisLeves.append(pessoas[contador][0])

print(f'O menor peso foi de {menor}Kg. Peso de {maisLeves}')
