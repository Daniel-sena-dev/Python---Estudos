pessoas = {
    'nomes': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(pessoas) # printa tudo
print(pessoas['nomes']) # printa somente o nome
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]} anos') # printa o nome e a idade
print(pessoas.keys()) # printa somente as chaves(keys) == nome do indice
print(pessoas.values()) # printa os valores que estão armazenados nas chaves
print(pessoas.items()) # printa as chaves e os valores
print('-=-' * 10)
pessoas['peso'] = 100
for chaves, valores in pessoas.items():
    print(f'{chaves}: {valores}')



