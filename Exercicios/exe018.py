# Exercicios de estrutura sequencial do site python Brasil
print('8- Programa para calcular salario')
horas = float(input('Digite as horas trabalhadas: '))
salario = float(input('Digite o salario por hora: '))
print(f'O salario do funcionario é de R${horas * salario:.02f}')
print('-' * 40)

print('9- fahrenheit para celsius ')
fahrenheit = float(input('Digite a temperatura: '))
convertCelsius = 5 * ((fahrenheit-32) / 9)
print(f'{convertCelsius:.02f}Cº')
print('-' * 40)

print('10- Celsius para fahrenheit')
celsius = float(input('Digite a temperatura: '))
convertFahrenheit = (celsius * (9/5) + 32)
print(f'{convertFahrenheit:.02f}Fº')
print('-' * 40)
