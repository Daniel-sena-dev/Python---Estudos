salario = float(input('Digite o salario do funcionario: '))

if salario > 1250:
    aumentoSalario = salario * 0.10
    print(f'O salario total do funcionario é de R${salario + aumentoSalario:.02f}')
else:
    aumentoSalario = salario * 0.15
    print(f'O salario total do funcionario é de R${salario + aumentoSalario:.02f}')

