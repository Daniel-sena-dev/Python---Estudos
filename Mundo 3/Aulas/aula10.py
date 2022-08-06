estado = dict()
brasil = list()

for contador in range(0, 3):
    estado['UF'] = input('Digite o nome do seu estado: ')
    estado['Sigla'] = input('Digite a sigla do seu estado: ')
    brasil.append(estado.copy())

for lista in brasil:
    for chaves, valor in lista.items():
        print(f'O campo {chaves} tem valor {valor} ')