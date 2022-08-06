
listaGeral = list()
cadastroPessoas = dict()
pessoa = media = 0
maiorMedia = list()

while True:
    pessoa += 1
    cadastroPessoas['nome'] = input(f'Digite o nome da {pessoa}º pessoa: ')

    # Validando o sexo
    while True:
        sexo = input(f'Digite o sexo de {cadastroPessoas["nome"]} [M/F] ').upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
        print('VALOR INVALIDO! DIGITE NOVAMENTE')
    cadastroPessoas['sexo'] = sexo

    cadastroPessoas['idade'] = int(input(f'Digite a idade de {cadastroPessoas["nome"]}: '))
    media += cadastroPessoas['idade']

    listaGeral.append(cadastroPessoas.copy())

    #CONTINUAR?
    while True:
        continuar = input('Deseja continuar? digite sim ou não [S/N] ').upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('VALOR INVALIDO! DIGITE NOVAMENTE')

    if continuar == 'N':
        break

print('-=-' * 10)
# A) QUANTAS PESSOAS FORAM CADASTRADAS?
print(f'Foi cadastrado um total de {pessoa}.')

# B) MEDIA DA IDADE DAS PESSOAS
media /= pessoa
print(f'A média de idade é {media:.02f}')

# C) MULHERES CADASTRADAS
print(f'As mulheres cadastradas foram: ', end=' ')
for p in listaGeral:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print('')

# D) lista das pessoas que estão acima da média:
for p in listaGeral:
    if p['idade'] >= media:
        print('       ', end='')
        for chaves, valor in p.items():
            print(f'{chaves} = {valor}; ', end=' ')
        print()
print('<<< ENCERRADO >>>')