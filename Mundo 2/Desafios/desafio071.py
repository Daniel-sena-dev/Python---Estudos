valorSacado = 0
cedulaCinquenta = 0
cedulaVinte = 0
cedulaDez = 0
cedulaUm = 0

while True:
    print('=' * 30)
    print('Bem vindo ao banco 24 horas!')
    valorSacado = int(input('Digite o valor a ser sacado: R$ '))
    #Verificando dados
    while valorSacado < 0:
        print('\033[1;33mValor digitado invalido!\033[m')
        valorSacado = int(input('Digite o valor a ser sacado: R$ '))
    print('=' * 30)
    #CEDULAS
    if valorSacado // 50:
        cedulaCinquenta = valorSacado // 50
        valorSacado = valorSacado - (valorSacado // 50) * 50
    if valorSacado // 20:
        cedulaVinte = valorSacado // 20
        valorSacado = valorSacado - (valorSacado // 20) * 20
    if valorSacado // 10:
        cedulaDez = valorSacado // 10
        valorSacado = valorSacado - (valorSacado // 10) * 10
    if valorSacado // 1:
        cedulaUm = valorSacado // 1
        valorSacado = valorSacado - (valorSacado // 1) / 1
        print('=' * 30)
    break

if cedulaCinquenta > 0:
    print(f'Total de {cedulaCinquenta} cédulas de R$50')
if cedulaVinte > 0:
    print(f'Total de {cedulaVinte} cédulas de R$20')
if cedulaDez > 0:
    print(f'Total de {cedulaDez} cédulas de R$10')
if cedulaUm > 0:
    print(f'Total de {cedulaUm} cédulas de R$1')
print('=' * 30)
print('Volte sempre! Banco 24 horas agradece a preferencia')
