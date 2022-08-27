print('3- programa para validar informações: ')
while True:
    try:
        nome = str(input('Digite seu nome: '))
    except ValueError:
        print('ERRO! Valor digitado invalido')
    else:
        if len(nome) > 3:
            break

while True:
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('ERRO! Valor digitado invalido')
    else:
        if 0 < idade <= 150:
            break

while True:
    try:
        salario = float(input('Digite seu salario: '))
    except ValueError:
        print('ERRO! Valor digitado invalido')
    else:
        if salario > 0:
            break

while True:
    try:
        sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0]
    except ValueError:
        print('ERRO! Valor digitado invalido')
    else:
        if sexo in 'MF':
            break

while True:
    try:
        estadoCivil = str(input('Digite seu estado civil [S/C/V/D]: ')).upper()[0]
    except ValueError:
        print('ERRO! Valor digitado invalido')
    else:
        if estadoCivil in 'SCVD':
            break
print(f'Cadastro realizado com sucesso!')
print(f'Nome: {nome}\nIdade: {idade}\nSalário: R${salario:.02f}\nSexo: {sexo}\nEstado Civil: {estadoCivil}')
