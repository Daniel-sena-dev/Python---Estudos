print('3- programa para verificar o sexo da pessoa M/F')
sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0]

if sexo == 'M':
    print('Sexo Masculino')
elif sexo == 'F':
    print('Sexo Feminino')
else:
    print('Inválido')
