print('12- Programa para calcular folha de pagamento 2.0v')
salarioHora = float(input('Digite o salário por hora do funcionario: '))
horas = float(input('Digite as horas trabalhadas: '))
salarioBruto = horas * salarioHora
INSS = FGTS = totalDescontos = salarioLiquido = 0

if salarioBruto <= 900:
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    totalDescontos = INSS + FGTS
    salarioLiquido = salarioBruto - totalDescontos
elif salarioBruto <= 1500:
    IR = salarioBruto * 0.05
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    totalDescontos = INSS + FGTS + IR
    salarioLiquido = salarioBruto - totalDescontos
elif salarioBruto <= 2500:
    IR = salarioBruto * 0.1
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    totalDescontos = INSS + FGTS + IR
    salarioLiquido = salarioBruto - totalDescontos
else:
    IR = salarioBruto * 0.2
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    totalDescontos = INSS + FGTS + IR
    salarioLiquido = salarioBruto - totalDescontos

print(f'Salário Bruto: R${salarioBruto:.02f}')
print(f'(-) IR: R${IR:.02f}')
print(f'(-) INSS (10%): R${INSS:.02f}')
print(f'FGTS: R${FGTS:.02f}')
print(f'Total de descontos: R${totalDescontos:.02f}')
print(f'Salário Liquido: R${salarioLiquido:.02f}')
