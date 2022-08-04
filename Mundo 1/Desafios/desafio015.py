dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
totalPagarDia = 60 * dias
totalPagarKm = Km * 0.15
total = totalPagarKm + totalPagarDia
print(f'Você alugou o carro por {dias} e rodou {Km}, o total foi de R$ {total:.02f}')
