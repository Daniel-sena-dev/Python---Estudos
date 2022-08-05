#Listas compostas
pessoas = [['Daniel', 23], ['Joao', 26], ['Joaquim', 13], ['Maria', 45]]

for contador in range(0, 4):
    print(pessoas[contador][0])

print('')
for dados in pessoas:
    print(f'{dados[0]} tem {dados[1]} anos')

print('Acabou a lista de nomes')
#=================================================
galera = list()
dado = list()
for contador in range(0, 3):
    dado.append(input('Digite o nome: '))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
#=====================================================
for pessoa in pessoas:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
    else:
        print(f'{pessoa[0]}  é menor de idade')