distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    precoViagem = 0.50 * distancia
    print(f'O valor da viagem ficou R${precoViagem:.02f}')
else:
    precoViagem = 0.45 * distancia
    print(f'O valor da viagem ficou R$ {precoViagem:.02f}')
