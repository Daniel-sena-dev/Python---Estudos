print(f'16- Calculo de comissao: ')
vendedores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
semanaTrabalhada = vendasBruta = totalSalario = 0
saida = ''
sair = False
while True:
    if sair:
        break

    vendasBruta = float(input('Digite o salario bruto: '))
    semanaTrabalhada = int(input('Digite a semana trabalhada: '))

    totalSalario = 200 * semanaTrabalhada
    totalSalario += vendasBruta * 0.09

    print(f'O salario da semana do funcionario foi de R${totalSalario:.02f}')

    if 200 <= totalSalario <= 299:
        vendedores[0] += 1
    elif 300 <= totalSalario <= 399:
        vendedores[1] += 1
    elif 400 <= totalSalario <= 499:
        vendedores[2] += 1
    elif 500 <= totalSalario <= 599:
        vendedores[3] += 1
    elif 600 <= totalSalario <= 699:
        vendedores[4] += 1
    elif 700 <= totalSalario <= 799:
        vendedores[5] += 1
    elif 800 <= totalSalario <= 899:
        vendedores[6] += 1
    elif 900 <= totalSalario <= 999:
        vendedores[7] += 1
    elif totalSalario >= 1000:
        vendedores[8] += 1

    #Sair do loop
    while True:
        try:
            saida = str(input('Deseja continuar? [S/N]')).upper()[0]
        except ValueError:
            print('ERRO! Valor invalido')
        else:
            if saida == 'N':
                sair = True
                break
            else:
                break

print(vendedores)