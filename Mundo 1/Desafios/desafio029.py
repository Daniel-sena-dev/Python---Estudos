velocidade = float(input('Digite a velocidade que estava seu carro: '))
multa = 7

if velocidade > 80:
    multaTotal = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade da via, o valor da multa é de R$ {multaTotal:.02f}')
