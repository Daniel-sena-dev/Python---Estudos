print('25- Programa para pedir idade, e no final verificar a mediaVeiculos das idades: ')
quantidadePessoas = int(input('Digite a quantidade de pessoas que deseja cadastrar: '))
mediaIdade = 0

for cont in range(0, quantidadePessoas):
    idade = int(input('Digite a idade: '))
    mediaIdade += idade

mediaGeral = mediaIdade / quantidadePessoas

if 0 <= mediaGeral <= 25:
    print(f'A turma é jovem, a mediaVeiculos foi {mediaGeral}')
elif 26 <= mediaGeral <= 60:
    print(f'A turma é adulta, a mediaVeiculos foi {mediaGeral}')
else:
    print(f'A turma é idosa, a mediaVeiculos foi {mediaGeral}')
