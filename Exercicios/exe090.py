print('38- Programa para calcular aumento salarial: ')
salario = float(input('Digite o salario do funcionario'))
salarioAtualizado = salario + (salario * 0.015)
anos = int(input('Digite a quantidade de anos trabalhados: '))
aumento = 0.015
for cont in range(0, anos):
    aumento *= 2
    salarioAtualizado += salarioAtualizado * aumento
    print(f'O salario do ano {cont + 1} é de R${salarioAtualizado:.02f}')
