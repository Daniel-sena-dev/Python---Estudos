print('13- Programa para dia da semana')
diaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
dia = int(input('Digite um numero de 1 a 7: '))
if dia < 0 or dia > 8:
    print(f'Numero invalido')
else:
    print(diaSemana[dia-1])
