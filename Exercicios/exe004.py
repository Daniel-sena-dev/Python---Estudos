def nomeDoMes(numMes):
    meses = ['', 'Janeiro', 'Fevereiro', 'Março',
             'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']

    return meses[numMes]

numMes = int(input('Digite o numero do mês: '))
mes = nomeDoMes(numMes)
print(mes)