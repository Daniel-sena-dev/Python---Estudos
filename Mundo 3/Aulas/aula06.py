# Dicionario- Variaveis compostas

#dados = dict()
dados = {
    'nome': 'Pedro',
    'idade': 25,

}

print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'

print(dados['sexo'])
del dados ['sexo']

#===============================
filme = {
    'titulo': 'star wars',
    'ano': 1977,
    'diretor': 'George Lucas'

}
print(filme.values()) #todos os valores do dicionario
print(filme.keys()) #nomes do indices
print(filme.items()) #keys + items
print('-=-'*10)
for key, valor in filme.items():
    print(f'O {key} é {valor}')
