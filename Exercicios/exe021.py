print(f'15- Programa salario 2.0v')
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
ganhosHoras = 10
print('-' * 40)
print(f'{"SALARIO BRUTO":>25}')
salarioBruto = horasTrabalhadas * ganhosHoras
print(f'O salario bruto é de: R${salarioBruto:.02f}')
print('-' * 40)
print(f'{"QUANTO PAGOU AO IMPOSTO DE RENDA":>8}')
impostoRenda = salarioBruto * 0.11
print(f'Imposto de renda: R${impostoRenda:.02f}')
print('-' * 40)
print(f'{"QUANTO PAGOU AO INSS":>10}')
INSS = salarioBruto * 0.08
print(f'O valor do INSS: R${INSS:0.02f}')
print('-' * 40)
print(f'{"QUANTO PAGOU AO SINDICATO"}')
sindicato = salarioBruto * 0.05
print(f'O valor do sindicato: R${sindicato:.02f}')
print('-' * 40)
print(f'{"SALARIO LIQUIDO"}')
salarioLiquido = salarioBruto - (impostoRenda + INSS + sindicato)
print(f'O salario liquido é: R${salarioLiquido:.02f}')
print('-' * 40)
