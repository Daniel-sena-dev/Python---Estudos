print(f'14- Programa para solucionar crimes: ')
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?',
             'Devia para a vítima?', 'Já trabalhou com a vítima?']
classificacao = 0

for cont in range(0, 5):
    print(perguntas[cont])
    resposta = str(input('Sim ou Não [S/N]? ')).upper()[0]
    if resposta == 'S':
        classificacao += 1

if classificacao == 2:
    print('Suspeito')
elif 3 <= classificacao <= 4:
    print('Cúmplice')
elif classificacao == 5:
    print('Assassino')
else:
    print('Inocente')