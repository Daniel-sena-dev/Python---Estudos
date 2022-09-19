print('13- programa para calcular a media anual de temperaturas: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperaturas = list()
media = 0

for cont in range(0, 12):
    temperaturas.append(float(input(f'Digite a temperatura do mês {meses[cont]}: ')))
    media += temperaturas[cont]
media /= 12

for cont in range(0, 12):
    if temperaturas[cont] > media:
        print(f'O mes {meses[cont]} teve {temperaturas[cont]:.02f}º, a media anual foi {media:.02f}')
