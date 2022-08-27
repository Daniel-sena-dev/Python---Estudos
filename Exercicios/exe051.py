print('27- Programa para feira de frutas: ')
kgMorangos = float(input('Digite a quantidade em kg de morangos: '))
kgMaca = float(input('Digite a quantidade em kg de maçãs: '))
valorTotal = 0

if kgMorangos <= 5:
    valorTotal = kgMorangos * 2.5
else:
    valorTotal = kgMorangos * 2.2

if kgMaca <= 5:
    valorTotal += kgMaca * 1.8
else:
    valorTotal += kgMaca * 1.5

if valorTotal > 25 or kgMaca + kgMorangos > 8:
    valorTotal -= (valorTotal * 0.1)

print(f'O valor total a ser pago é de R${valorTotal:.02f}')