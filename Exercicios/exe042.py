print('18- Programa para validar data')
dia = int(input('Digite um dia: '))
mes = int(input('Digite um mes: '))
ano = int(input('Digite um ano: '))

if 0 < dia < 31 and mes != 2 and ano > 0:
    print(f'{dia}/{mes}/{ano}')
elif mes == 2 and 0 < dia < 29:
    print(f'{dia}/{mes}/{ano}')
else:
    print(f'Data digitada invalida! ')
