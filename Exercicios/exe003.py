def calcularSalario(quanHoras, salaHora):
    salario = quanHoras * salaHora
    return f'Salário igual a R$ {salario:.02f}'


quanHoras = int(input('Digite a quantidade de horas trabalhadas: '))
salaHora = float(input('Digite o valor do salario por hora: '))
print(calcularSalario(quanHoras, salaHora))
